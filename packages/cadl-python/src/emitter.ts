import { getPagedResult } from "@azure-tools/cadl-azure-core";
import {
  EnumMemberType,
  EnumType,
  getDoc,
  getFriendlyName,
  getIntrinsicModelName,
  getMaxLength,
  getMaxValue,
  getMinLength,
  getMinValue,
  getPattern,
  getServiceNamespace,
  getServiceNamespaceString,
  getServiceTitle,
  getSummary,
  getVisibility,
  ignoreDiagnostics,
  isErrorModel,
  isNeverType,
  ModelType,
  ModelTypeProperty,
  NamespaceType,
  Program,
  resolvePath,
  Type,
} from "@cadl-lang/compiler";
import { getDiscriminator } from "@cadl-lang/rest";
import {
  getAllRoutes,
  getContentTypes,
  getServers,
  HttpOperationParameter,
  HttpOperationParameters,
  HttpOperationResponse,
  HttpOperationResponseContent,
  HttpServer,
  OperationDetails,
} from "@cadl-lang/rest/http";
import { getAddedOn } from "@cadl-lang/versioning";
import { execFileSync } from "child_process";
import { dump } from "js-yaml";
import { dirname, resolve } from "path";
import { fileURLToPath } from "url";

interface HttpServerParameter {
  type: "endpointPath";
  name: string;
  param: ModelTypeProperty;
}

export async function $onEmit(program: Program) {
  const yamlMap = createYamlEmitter(program);
  const yamlPath = resolvePath(program.compilerOptions.outputPath!, "output.yaml");
  await program.host.writeFile(yamlPath, dump(yamlMap));
  const __dirname = dirname(fileURLToPath(import.meta.url));
  const root = resolve(__dirname, "..", "..");

  execFileSync(process.execPath, [
    `${root}/node_modules/@autorest/python/run-python3.js`,
    `${root}/node_modules/@autorest/python/run_cadl.py`,
    `--output-folder=${program.compilerOptions.outputPath!}`,
    `--cadl-file=${yamlPath}`,
  ]);
}

function camelToSnakeCase(name: string): string {
  const camelToSnakeCaseRe = (str: string) =>
    str
      .replace(/\s+/g, "_")
      .replace(/\$/g, "")
      .replace(/-/g, "_")
      .replace(/[A-Z]/g, (letter) => `_${letter.toLowerCase()}`);

  return camelToSnakeCaseRe(name[0].toLowerCase() + name.slice(1));
}

const typesMap = new Map<Type, Record<string, any>>();
const simpleTypesMap = new Map<string, Record<string, any>>();
const endpointPathParameters: Record<string, any>[] = [];

function isSimpleType(program: Program, modelTypeProperty: ModelTypeProperty | undefined): boolean {
  // these decorators can only work for simple type(int/string/float, etc)
  if (modelTypeProperty) {
    const funcs = [getMinValue, getMaxValue, getMinLength, getMaxLength, getPattern];
    for (const func of funcs) {
      if (func(program, modelTypeProperty)) {
        return true;
      }
    }
  }
  return false;
}

function getDocStr(program: Program, target: Type): string {
  return getDoc(program, target) ?? "";
}

function getOperationGroupName(program: Program, operation: OperationDetails): string {
  let groupName = "";
  const serviceNamespace = getServiceNamespace(program);
  if (!serviceNamespace || capitalize(operation.container.name) !== capitalize(serviceNamespace.name)) {
    groupName = capitalize(operation.container.name);
  }
  return groupName;
}

function handleDiscriminator(program: Program, type: ModelType, model: Record<string, any>) {
  const discriminator = getDiscriminator(program, type);
  if (discriminator) {
    let discriminatorProperty;
    for (const childModel of type.derivedModels) {
      const modelType = getType(program, childModel);
      for (const property of modelType.properties) {
        if (property.restApiName === discriminator.propertyName) {
          modelType.discriminatorValue = property.type.value;
          property.isDiscriminator = true;
          model.discriminatedSubtypes[property.type.value] = modelType;
          discriminatorProperty = property;
        }
      }
    }
    // it is not included in properties of cadl but needed by python codegen
    if (discriminatorProperty) {
      const propertyCopy = { ...discriminatorProperty, isPolymorphic: true };
      propertyCopy.description = "";
      model.properties.push(propertyCopy);
    }
  }
}

function getType(program: Program, type: Type, modelTypeProperty: ModelTypeProperty | undefined = undefined): any {
  // don't cache simple type(string, int, etc) since decorators may change the result
  const enableCache = !isSimpleType(program, modelTypeProperty);
  if (enableCache) {
    const cached = typesMap.get(type);
    if (cached) {
      return cached;
    }
  }
  let newValue = emitType(program, type, modelTypeProperty);
  if (enableCache) {
    typesMap.set(type, newValue);
    if (type.kind === "Model") {
      // need to do properties after insertion to avoid infinite recursion
      for (const property of type.properties.values()) {
        newValue.properties.push(emitProperty(program, property));
      }
      // need to do discriminator outside `emitModel` to avoid infinite recursion
      handleDiscriminator(program, type, newValue);
    }
  } else {
    const key = dump(newValue, { sortKeys: true });
    const value = simpleTypesMap.get(key);
    if (value) {
      newValue = value;
    } else {
      simpleTypesMap.set(key, newValue);
    }
  }

  return newValue;
}

// To pass the yaml dump
function getAddedOnVersion(p: Program, t: Type): string | undefined {
  return getAddedOn(p as any, t as any)?.value;
}

function emitParamBase(program: Program, parameter: ModelTypeProperty | Type): Record<string, any> {
  let optional: boolean;
  let name: string;
  let description: string = "";
  let addedApiVersion: string | undefined;

  if (parameter.kind === "ModelProperty") {
    optional = parameter.optional;
    name = parameter.name;
    description = getDocStr(program, parameter);
    addedApiVersion = getAddedOnVersion(program, parameter);
  } else {
    optional = false;
    name = "body";
  }

  return {
    optional,
    description,
    addedApiVersion,
    clientName: camelToSnakeCase(name),
    inOverload: false,
  };
}

function emitBodyParameter(program: Program, bodyType: Type, params: HttpOperationParameters): Record<string, any> {
  const base = emitParamBase(program, params.bodyParameter ?? bodyType);
  const contentTypeParam = params.parameters.find((p) => p.type === "header" && p.name === "content-type");
  const contentTypes = contentTypeParam
    ? ignoreDiagnostics(getContentTypes(contentTypeParam.param))
    : ["application/json"];
  if (contentTypes.length !== 1) {
    throw Error("Currently only one kind of content-type!");
  }
  let type;
  if (params.bodyParameter) {
    type = getType(program, params.bodyParameter.type, params.bodyParameter);
  } else {
    type = getType(program, bodyType);
  }
  return {
    contentTypes,
    type,
    restApiName: params.bodyParameter?.name ?? "body",
    location: "body",
    ...base,
    defaultContentType: contentTypes.includes("application/json") ? "application/json" : contentTypes[0],
  };
}

function emitParameter(
  program: Program,
  parameter: HttpOperationParameter | HttpServerParameter,
  implementation: string,
): Record<string, any> {
  const base = emitParamBase(program, parameter.param);
  let type = getType(program, parameter.param.type, parameter.param);
  let clientDefaultValue = undefined;
  if (parameter.name.toLowerCase() === "content-type" && type["type"] === "constant") {
    /// We don't want constant types for content types, so we make sure if it's
    /// a constant, we make it not constant
    clientDefaultValue = type["value"];
    type = type["valueType"];
  }
  const paramMap: Record<string, any> = {
    restApiName: parameter.name,
    location: parameter.type,
    type: type,
    implementation: implementation,
  };

  if (paramMap.type.type === "constant") {
    clientDefaultValue = paramMap.type.value;
  }
  return { clientDefaultValue, ...base, ...paramMap };
}

function emitContentTypeParameter(
  bodyParameter: Record<string, any>,
  inOverload: boolean,
  inOverriden: boolean,
): Record<string, any> {
  return {
    checkClientInput: false,
    clientDefaultValue: bodyParameter.defaultContentType,
    clientName: "content_type",
    delimiter: null,
    description: `Body parameter Content-Type. Known values are: ${bodyParameter.contentTypes}.`,
    implementation: "Method",
    inDocstring: true,
    inOverload: inOverload,
    inOverriden: inOverriden,
    location: "header",
    optional: true,
    restApiName: "Content-Type",
    type: KnownTypes.string,
  };
}

function emitAcceptParameter(inOverload: boolean, inOverriden: boolean): Record<string, any> {
  return {
    checkClientInput: false,
    clientDefaultValue: "application/json",
    clientName: "accept",
    delimiter: null,
    description: "Accept header.",
    explode: false,
    groupedBy: null,
    implementation: "Method",
    inDocstring: true,
    inOverload: inOverload,
    inOverriden: inOverriden,
    location: "header",
    optional: false,
    restApiName: "Accept",
    skipUrlEncoding: false,
    type: ConstantTypes.applicationJson,
  };
}

function emitResponseHeaders(program: Program, headers?: Record<string, ModelTypeProperty>): Record<string, any>[] {
  const retval: Record<string, any>[] = [];
  if (!headers) {
    return retval;
  }
  for (const [key, value] of Object.entries(headers)) {
    retval.push({
      type: emitType(program, value.type, value),
      restApiName: key,
    });
  }
  return retval;
}

function emitResponse(
  program: Program,
  response: HttpOperationResponse,
  innerResponse: HttpOperationResponseContent,
): Record<string, any> {
  let type = undefined;
  if (innerResponse.body?.type) {
    type = getType(program, innerResponse.body.type);
  }
  const statusCodes = [];
  if (response.statusCode === "*") {
    statusCodes.push("default");
  } else {
    statusCodes.push(parseInt(response.statusCode));
  }
  return {
    headers: emitResponseHeaders(program, innerResponse.headers),
    statusCodes: statusCodes,
    addedApiVersion: getAddedOnVersion(program, response.type),
    discriminator: "basic",
    type: type,
  };
}

function emitOperation(program: Program, operation: OperationDetails) {
  if (getPagedResult(program, operation.operation)) {
    return emitPagingOperation(program, operation);
  }
  return emitBasicOperation(program, operation);
}

function addPagingInformation(program: Program, operation: OperationDetails, emittedOperation: Record<string, any>) {
  emittedOperation["discriminator"] = "paging";
  const pagedResult = getPagedResult(program, operation.operation);
  if (pagedResult === undefined) {
    throw Error("Trying to add paging information, but not paging metadata for this operation");
  }
  emittedOperation["itemName"] = pagedResult.itemsPath;
  emittedOperation["continuationTokenName"] = pagedResult.nextLinkPath;
}

function emitPagingOperation(program: Program, operation: OperationDetails): Record<string, any> {
  const emittedOperation = emitBasicOperation(program, operation);
  addPagingInformation(program, operation, emittedOperation);
  return emittedOperation;
}

function emitBasicOperation(program: Program, operation: OperationDetails): Record<string, any> {
  // Set up parameters for operation
  const parameters: Record<string, any>[] = [];
  if (endpointPathParameters) {
    for (const param of endpointPathParameters) {
      parameters.push(param);
    }
  }
  for (const param of operation.parameters.parameters) {
    parameters.push(emitParameter(program, param, "Method"));
  }

  // Set up responses for operation
  const responses: Record<string, any>[] = [];
  const exceptions: Record<string, any>[] = [];
  const isOverload: boolean = false;
  const isOverriden: boolean = false;
  for (const response of operation.responses) {
    for (const innerResponse of response.responses) {
      const emittedResponse = emitResponse(program, response, innerResponse);
      if (emittedResponse["type"] && parameters.filter((e) => e.restApiName.toLowerCase() === "accept").length === 0) {
        parameters.push(emitAcceptParameter(isOverload, isOverriden));
      }
      if (isErrorModel(program, response.type)) {
        // * is valid status code in cadl but invalid for autorest.python
        if (response.statusCode === "*") {
          exceptions.push(emittedResponse);
        }
      } else {
        responses.push(emittedResponse);
      }
    }
  }

  let bodyParameter: Record<string, any> | undefined;
  if (operation.parameters.bodyType === undefined) {
    bodyParameter = undefined;
  } else {
    bodyParameter = emitBodyParameter(program, operation.parameters.bodyType, operation.parameters);
    if (parameters.filter((e) => e.restApiName.toLowerCase() === "content-type").length === 0) {
      parameters.push(emitContentTypeParameter(bodyParameter, isOverload, isOverriden));
    }
  }
  return {
    name: camelToSnakeCase(operation.operation.name),
    description: getDocStr(program, operation.operation),
    summary: getSummary(program, operation.operation),
    url: operation.path,
    method: operation.verb.toUpperCase(),
    parameters: parameters,
    bodyParameter: bodyParameter,
    responses: responses,
    exceptions: exceptions,
    groupName: getOperationGroupName(program, operation),
    addedApiVersion: getAddedOnVersion(program, operation.operation),
    discriminator: "basic",
    isOverload: false,
    overloads: [],
    apiVersions: [getAddedOnVersion(program, operation.operation)],
  };
}

function emitString(program: Program, modelTypeProperty: ModelTypeProperty | undefined): Record<string, any> {
  let maxLength = undefined;
  let minLength = undefined;
  let pattern = undefined;
  if (modelTypeProperty) {
    maxLength = getMaxLength(program, modelTypeProperty);
    minLength = getMinLength(program, modelTypeProperty);
    pattern = getPattern(program, modelTypeProperty);
  }
  if (!(maxLength || minLength || pattern)) {
    return KnownTypes.string;
  }
  return { minLength, maxLength, pattern, type: "string" };
}

function emitNumber(
  type: string,
  program: Program,
  modelTypeProperty: ModelTypeProperty | undefined,
): Record<string, any> {
  let minimum = undefined;
  let maximum = undefined;
  if (modelTypeProperty) {
    minimum = getMinValue(program, modelTypeProperty);
    maximum = getMaxValue(program, modelTypeProperty);
  }

  if (!(maximum || minimum)) {
    return { type };
  }
  return { minimum, maximum, type };
}

function isReadOnly(program: Program, type: ModelTypeProperty): boolean {
  const visibility = getVisibility(program, type);
  if (visibility) {
    return !visibility.includes("write");
  } else {
    return false;
  }
}

function emitProperty(program: Program, property: ModelTypeProperty): Record<string, any> {
  let clientDefaultValue = undefined;
  const propertyDefaultKind = property.default?.kind;
  if (
    property.default &&
    (propertyDefaultKind === "Number" || propertyDefaultKind === "String" || propertyDefaultKind == "Boolean")
  ) {
    clientDefaultValue = property.default.value;
  }
  return {
    clientName: camelToSnakeCase(property.name),
    restApiName: property.name,
    type: getType(program, property.type, property),
    optional: property.optional,
    description: getDocStr(program, property),
    addedApiVersion: getAddedOnVersion(program, property),
    readonly: isReadOnly(program, property),
    clientDefaultValue: clientDefaultValue,
  };
}

function getName(program: Program, type: ModelType): string {
  const friendlyName = getFriendlyName(program, type);
  if (friendlyName) {
    return friendlyName;
  } else {
    if (type.templateArguments && type.templateArguments.length > 0) {
      return type.name + type.templateArguments.map((it) => (it.kind === "Model" ? it.name : "")).join("");
    } else {
      return type.name;
    }
  }
}

function emitModel(
  program: Program,
  type: ModelType,
  modelTypeProperty: ModelTypeProperty | undefined,
): Record<string, any> {
  if (type.indexer) {
    if (isNeverType(type.indexer.key)) {
    } else {
      const name = getIntrinsicModelName(program, type.indexer.key);
      if (name === "string") {
        return { type: "dict", elementType: getType(program, type.indexer.value!) };
      } else if (name === "integer") {
        return { type: "list", elementType: getType(program, type.indexer.value!) };
      }
    }
  }

  for (const decorator of type.decorators) {
    if (decorator.decorator.name === "$knownValues") {
      for (const arg of decorator.args) {
        if (typeof arg.value === "object" && arg.value.kind === "Enum") {
          const enumResult = emitEnum(program, arg.value);
          enumResult["name"] = type.name;
          return enumResult;
        }
      }
    }
  }
  const name = getIntrinsicModelName(program, type);
  switch (name) {
    case "bytes":
      return { type: "byte-array", format: "byte" };
    case "int8":
    case "int16":
    case "int32":
    case "int64":
    case "safeint":
    case "uint8":
    case "uint16":
    case "uint32":
    case "uint64":
      return emitNumber("integer", program, modelTypeProperty);
    case "float32":
    case "float64":
      return emitNumber("float", program, modelTypeProperty);
    case "string":
      return emitString(program, modelTypeProperty);
    case "boolean":
      return { type: "boolean" };
    case "plainDate":
      return { type: "date" };
    case "zonedDateTime":
      return { type: "datetime", format: "date-time" };
    case "plainTime":
      return { type: "time" };
    case "duration":
      return { type: "duration" };
    default:
      // Now we know it's a defined model
      // const discriminator = getDiscriminator(program, type);
      // const discriminatorEntry: Record<string, any> | undefined = {};
      // const childModels: Record<string, any>[] = [];
      // for (const childModel of type.derivedModels) {
      //   childModels.push(getType(program, childModel));
      // }
      // if (discriminator) {
      //   const discriminatorMapping = getDiscriminatorMapping(program, discriminator, childModels);
      //   if (discriminatorMapping) {
      //     discriminatorEntry.mapping = discriminatorMapping;
      //   }
      //   discriminatorEntry.propertyName = discriminator.propertyName;
      // }
      const properties: Record<string, any>[] = [];
      let baseModel = undefined;
      if (type.baseModel) {
        baseModel = getType(program, type.baseModel);
      }
      const modelName = getName(program, type);
      return {
        type: "model",
        name: modelName,
        description: getDocStr(program, type),
        parents: baseModel ? [baseModel] : [],
        discriminatedSubtypes: {},
        properties: properties,
        addedApiVersion: getAddedOnVersion(program, type),
        snakeCaseName: camelToSnakeCase(modelName),
      };
  }
}

function intOrFloat(value: number): string {
  return value.toString().indexOf(".") === -1 ? "integer" : "float";
}

function enumName(name: string): string {
  if (name.toUpperCase() === name) {
    return name;
  }
  return camelToSnakeCase(name).toUpperCase();
}

function emitEnum(program: Program, type: EnumType): Record<string, any> {
  const enumValues = [];
  for (const m of type.members) {
    enumValues.push({
      name: enumName(m.name),
      value: m.value ?? m.name,
      description: getDocStr(program, m),
    });
  }

  return {
    type: "enum",
    name: type.name,
    description: getDocStr(program, type),
    valueType: { type: enumMemberType(type.members[0]) },
    values: enumValues,
  };
  function enumMemberType(member: EnumMemberType) {
    if (typeof member.value === "number") {
      return intOrFloat(member.value);
    }
    return "string";
  }
}

function constantType(value: any, valueType: string): Record<string, any> {
  return { type: "constant", value: value, valueType: { type: valueType } };
}

function emitType(
  program: Program,
  type: Type,
  modelTypeProperty: ModelTypeProperty | undefined = undefined,
): Record<string, any> {
  switch (type.kind) {
    case "Number":
      return constantType(type.value, intOrFloat(type.value));
    case "String":
      return constantType(type.value, "string");
    case "Boolean":
      return constantType(type.value, "boolean");
    case "Model":
      return emitModel(program, type, modelTypeProperty);
    case "Enum":
      return emitEnum(program, type);
    default:
      throw Error(`Not supported ${type.kind}`);
  }
}

function capitalize(name: string): string {
  return name[0].toUpperCase() + name.slice(1);
}

function emitOperationGroups(program: Program): Record<string, any>[] {
  const operationGroups: Record<string, any>[] = [];
  const allOperations = ignoreDiagnostics(getAllRoutes(program));
  for (const operation of allOperations) {
    let existingOperationGroup: Record<string, any> | undefined = undefined;
    for (const operationGroup of operationGroups) {
      if (operationGroup["className"] === getOperationGroupName(program, operation)) {
        existingOperationGroup = operationGroup;
      }
    }
    const emittedOperation = emitOperation(program, operation);
    if (existingOperationGroup) {
      existingOperationGroup["operations"].push(emittedOperation);
    } else {
      const newOperationGroup = {
        propertyName: getOperationGroupName(program, operation),
        className: getOperationGroupName(program, operation),
        operations: [emittedOperation],
      };
      operationGroups.push(newOperationGroup);
    }
  }
  return operationGroups;
}

function getServerHelper(program: Program, namespace: NamespaceType): HttpServer | undefined {
  const servers = getServers(program, namespace);
  if (servers === undefined) {
    return undefined;
  }
  return servers[0];
}

function emitGlobalParameters(program: Program, namespace: NamespaceType): Record<string, any>[] {
  const server = getServerHelper(program, namespace);
  if (server === undefined) {
    return [
      {
        optional: false,
        description: "Service host",
        clientName: "endpoint",
        clientDefaultValue: null,
        restApiName: "$host",
        location: "path",
        type: KnownTypes.string,
        implementation: "Client",
        inOverload: false,
      },
    ];
  }
  if (server.parameters) {
    const params: Record<string, any>[] = [];
    for (const param of server.parameters.values()) {
      const serverParameter: HttpServerParameter = {
        type: "endpointPath",
        name: param.name,
        param: param,
      };
      endpointPathParameters.push(emitParameter(program, serverParameter, "Client"));
      params.push(emitParameter(program, serverParameter, "Client"));
    }
    return params;
  } else {
    return [
      {
        optional: false,
        description: "Service host",
        clientName: "endpoint",
        clientDefaultValue: server.url,
        restApiName: "$host",
        location: "path",
        type: KnownTypes.string,
        implementation: "Client",
        inOverload: false,
      },
    ];
  }
}

function createYamlEmitter(program: Program) {
  const serviceNamespace = getServiceNamespace(program);
  if (serviceNamespace === undefined) {
    throw Error("Can not emit yaml for a namespace that doesn't exist.");
  }

  // let [_, versions] = getVersions(program, serviceNamespace);
  // if (versions.length === 0 && getServiceVersion(program)) {
  //   versions = [getServiceVersion(program)];
  // }
  const name = getServiceTitle(program).replace(/ /g, "");
  const clientParameters = emitGlobalParameters(program, serviceNamespace);
  // Get types
  const server = getServerHelper(program, serviceNamespace);
  const codeModel = {
    client: {
      name: name,
      description: "Service client",
      moduleName: camelToSnakeCase(name),
      parameters: clientParameters,
      security: {},
      namespace: getServiceNamespaceString(program),
      url: server ? server.url : "",
      apiVersions: [],
    },
    operationGroups: emitOperationGroups(program),
    types: [
      ...typesMap.values(),
      ...Object.values(KnownTypes),
      ...simpleTypesMap.values(),
      ...Object.values(ConstantTypes),
    ],
  };
  return codeModel;
}

const KnownTypes = {
  string: { type: "string" },
};

const ConstantTypes = {
  applicationJson: {
    apiVersions: [],
    clientDefaultValue: null,
    type: "constant",
    value: "application/json",
    valueType: KnownTypes.string,
    xmlMetadata: {},
  },
};
