# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.0.6246, generator: {generator})
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.core.exceptions import HttpResponseError
import msrest.serialization


class AnalyzeOperationResult(msrest.serialization.Model):
    """Status and result of the queued analyze operation.

    All required parameters must be populated in order to send to Azure.

    :param status: Required. Operation status. Possible values include: 'notStarted', 'running',
     'succeeded', 'failed'.
    :type status: str or ~azure.ai.formrecognizer.models.OperationStatus
    :param created_date_time: Required. Date and time (UTC) when the analyze operation was
     submitted.
    :type created_date_time: ~datetime.datetime
    :param last_updated_date_time: Required. Date and time (UTC) when the status was last updated.
    :type last_updated_date_time: ~datetime.datetime
    :param analyze_result: Results of the analyze operation.
    :type analyze_result: ~azure.ai.formrecognizer.models.AnalyzeResult
    """

    _validation = {
        'status': {'required': True},
        'created_date_time': {'required': True},
        'last_updated_date_time': {'required': True},
    }

    _attribute_map = {
        'status': {'key': 'status', 'type': 'str'},
        'created_date_time': {'key': 'createdDateTime', 'type': 'iso-8601'},
        'last_updated_date_time': {'key': 'lastUpdatedDateTime', 'type': 'iso-8601'},
        'analyze_result': {'key': 'analyzeResult', 'type': 'AnalyzeResult'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(AnalyzeOperationResult, self).__init__(**kwargs)
        self.status = kwargs.get('status', None)
        self.created_date_time = kwargs.get('created_date_time', None)
        self.last_updated_date_time = kwargs.get('last_updated_date_time', None)
        self.analyze_result = kwargs.get('analyze_result', None)


class AnalyzeResult(msrest.serialization.Model):
    """Analyze operation result.

    All required parameters must be populated in order to send to Azure.

    :param version: Required. Version of schema used for this result.
    :type version: str
    :param read_results: Required. Text extracted from the input.
    :type read_results: list[~azure.ai.formrecognizer.models.ReadResult]
    :param page_results: Page-level information extracted from the input.
    :type page_results: list[~azure.ai.formrecognizer.models.PageResult]
    :param document_results: Document-level information extracted from the input.
    :type document_results: list[~azure.ai.formrecognizer.models.DocumentResult]
    :param errors: List of errors reported during the analyze operation.
    :type errors: list[~azure.ai.formrecognizer.models.ErrorInformation]
    """

    _validation = {
        'version': {'required': True},
        'read_results': {'required': True},
    }

    _attribute_map = {
        'version': {'key': 'version', 'type': 'str'},
        'read_results': {'key': 'readResults', 'type': '[ReadResult]'},
        'page_results': {'key': 'pageResults', 'type': '[PageResult]'},
        'document_results': {'key': 'documentResults', 'type': '[DocumentResult]'},
        'errors': {'key': 'errors', 'type': '[ErrorInformation]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(AnalyzeResult, self).__init__(**kwargs)
        self.version = kwargs.get('version', None)
        self.read_results = kwargs.get('read_results', None)
        self.page_results = kwargs.get('page_results', None)
        self.document_results = kwargs.get('document_results', None)
        self.errors = kwargs.get('errors', None)


class DataTable(msrest.serialization.Model):
    """Information about the extracted table contained in a page.

    All required parameters must be populated in order to send to Azure.

    :param rows: Required. Number of rows.
    :type rows: int
    :param columns: Required. Number of columns.
    :type columns: int
    :param cells: Required. List of cells contained in the table.
    :type cells: list[~azure.ai.formrecognizer.models.DataTableCell]
    """

    _validation = {
        'rows': {'required': True, 'minimum': 1},
        'columns': {'required': True, 'minimum': 1},
        'cells': {'required': True},
    }

    _attribute_map = {
        'rows': {'key': 'rows', 'type': 'int'},
        'columns': {'key': 'columns', 'type': 'int'},
        'cells': {'key': 'cells', 'type': '[DataTableCell]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(DataTable, self).__init__(**kwargs)
        self.rows = kwargs.get('rows', None)
        self.columns = kwargs.get('columns', None)
        self.cells = kwargs.get('cells', None)


class DataTableCell(msrest.serialization.Model):
    """Information about the extracted cell in a table.

    All required parameters must be populated in order to send to Azure.

    :param row_index: Required. Row index of the cell.
    :type row_index: int
    :param column_index: Required. Column index of the cell.
    :type column_index: int
    :param row_span: Number of rows spanned by this cell.
    :type row_span: int
    :param column_span: Number of columns spanned by this cell.
    :type column_span: int
    :param text: Required. Text content of the cell.
    :type text: str
    :param bounding_box: Required. Bounding box of the cell.
    :type bounding_box: list[float]
    :param confidence: Required. Confidence value.
    :type confidence: float
    :param elements: When includeTextDetails is set to true, a list of references to the text
     elements constituting this table cell.
    :type elements: list[str]
    :param is_header: Is the current cell a header cell?.
    :type is_header: bool
    :param is_footer: Is the current cell a footer cell?.
    :type is_footer: bool
    """

    _validation = {
        'row_index': {'required': True, 'minimum': 0},
        'column_index': {'required': True, 'minimum': 0},
        'row_span': {'minimum': 1},
        'column_span': {'minimum': 1},
        'text': {'required': True},
        'bounding_box': {'required': True, 'max_items': 8, 'min_items': 8},
        'confidence': {'required': True, 'maximum': 1, 'minimum': 0},
    }

    _attribute_map = {
        'row_index': {'key': 'rowIndex', 'type': 'int'},
        'column_index': {'key': 'columnIndex', 'type': 'int'},
        'row_span': {'key': 'rowSpan', 'type': 'int'},
        'column_span': {'key': 'columnSpan', 'type': 'int'},
        'text': {'key': 'text', 'type': 'str'},
        'bounding_box': {'key': 'boundingBox', 'type': '[float]'},
        'confidence': {'key': 'confidence', 'type': 'float'},
        'elements': {'key': 'elements', 'type': '[str]'},
        'is_header': {'key': 'isHeader', 'type': 'bool'},
        'is_footer': {'key': 'isFooter', 'type': 'bool'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(DataTableCell, self).__init__(**kwargs)
        self.row_index = kwargs.get('row_index', None)
        self.column_index = kwargs.get('column_index', None)
        self.row_span = kwargs.get('row_span', 1)
        self.column_span = kwargs.get('column_span', 1)
        self.text = kwargs.get('text', None)
        self.bounding_box = kwargs.get('bounding_box', None)
        self.confidence = kwargs.get('confidence', None)
        self.elements = kwargs.get('elements', None)
        self.is_header = kwargs.get('is_header', False)
        self.is_footer = kwargs.get('is_footer', False)


class DocumentResult(msrest.serialization.Model):
    """A set of extracted fields corresponding to the input document.

    All required parameters must be populated in order to send to Azure.

    :param doc_type: Required. Document type.
    :type doc_type: str
    :param page_range: Required. First and last page number where the document is found.
    :type page_range: list[int]
    :param fields: Required. Dictionary of named field values.
    :type fields: dict[str, ~azure.ai.formrecognizer.models.FieldValue]
    """

    _validation = {
        'doc_type': {'required': True},
        'page_range': {'required': True, 'max_items': 2, 'min_items': 2},
        'fields': {'required': True},
    }

    _attribute_map = {
        'doc_type': {'key': 'docType', 'type': 'str'},
        'page_range': {'key': 'pageRange', 'type': '[int]'},
        'fields': {'key': 'fields', 'type': '{FieldValue}'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(DocumentResult, self).__init__(**kwargs)
        self.doc_type = kwargs.get('doc_type', None)
        self.page_range = kwargs.get('page_range', None)
        self.fields = kwargs.get('fields', None)


class ErrorInformation(msrest.serialization.Model):
    """ErrorInformation.

    All required parameters must be populated in order to send to Azure.

    :param code: Required.
    :type code: str
    :param message: Required.
    :type message: str
    """

    _validation = {
        'code': {'required': True},
        'message': {'required': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ErrorInformation, self).__init__(**kwargs)
        self.code = kwargs.get('code', None)
        self.message = kwargs.get('message', None)


class ErrorResponse(msrest.serialization.Model):
    """ErrorResponse.

    All required parameters must be populated in order to send to Azure.

    :param error: Required.
    :type error: ~azure.ai.formrecognizer.models.ErrorInformation
    """

    _validation = {
        'error': {'required': True},
    }

    _attribute_map = {
        'error': {'key': 'error', 'type': 'ErrorInformation'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ErrorResponse, self).__init__(**kwargs)
        self.error = kwargs.get('error', None)


class FieldValue(msrest.serialization.Model):
    """Recognized field value.

    All required parameters must be populated in order to send to Azure.

    :param type: Required. Type of field value. Possible values include: 'string', 'date', 'time',
     'phoneNumber', 'number', 'integer', 'array', 'object'.
    :type type: str or ~azure.ai.formrecognizer.models.FieldValueType
    :param value_string: String value.
    :type value_string: str
    :param value_date: Date value.
    :type value_date: ~datetime.date
    :param value_time: Time value.
    :type value_time: str
    :param value_phone_number: Phone number value.
    :type value_phone_number: str
    :param value_number: Floating point value.
    :type value_number: float
    :param value_integer: Integer value.
    :type value_integer: int
    :param value_array: Array of field values.
    :type value_array: list[~azure.ai.formrecognizer.models.FieldValue]
    :param value_object: Dictionary of named field values.
    :type value_object: dict[str, ~azure.ai.formrecognizer.models.FieldValue]
    :param text: Text content of the extracted field.
    :type text: str
    :param bounding_box: Bounding box of the field value, if appropriate.
    :type bounding_box: list[float]
    :param confidence: Confidence score.
    :type confidence: float
    :param elements: When includeTextDetails is set to true, a list of references to the text
     elements constituting this field.
    :type elements: list[str]
    :param page: The 1-based page number in the input document.
    :type page: int
    """

    _validation = {
        'type': {'required': True},
        'bounding_box': {'max_items': 8, 'min_items': 8},
        'confidence': {'maximum': 1, 'minimum': 0},
        'page': {'minimum': 1},
    }

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'value_string': {'key': 'valueString', 'type': 'str'},
        'value_date': {'key': 'valueDate', 'type': 'date'},
        'value_time': {'key': 'valueTime', 'type': 'str'},
        'value_phone_number': {'key': 'valuePhoneNumber', 'type': 'str'},
        'value_number': {'key': 'valueNumber', 'type': 'float'},
        'value_integer': {'key': 'valueInteger', 'type': 'int'},
        'value_array': {'key': 'valueArray', 'type': '[FieldValue]'},
        'value_object': {'key': 'valueObject', 'type': '{FieldValue}'},
        'text': {'key': 'text', 'type': 'str'},
        'bounding_box': {'key': 'boundingBox', 'type': '[float]'},
        'confidence': {'key': 'confidence', 'type': 'float'},
        'elements': {'key': 'elements', 'type': '[str]'},
        'page': {'key': 'page', 'type': 'int'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(FieldValue, self).__init__(**kwargs)
        self.type = kwargs.get('type', None)
        self.value_string = kwargs.get('value_string', None)
        self.value_date = kwargs.get('value_date', None)
        self.value_time = kwargs.get('value_time', None)
        self.value_phone_number = kwargs.get('value_phone_number', None)
        self.value_number = kwargs.get('value_number', None)
        self.value_integer = kwargs.get('value_integer', None)
        self.value_array = kwargs.get('value_array', None)
        self.value_object = kwargs.get('value_object', None)
        self.text = kwargs.get('text', None)
        self.bounding_box = kwargs.get('bounding_box', None)
        self.confidence = kwargs.get('confidence', None)
        self.elements = kwargs.get('elements', None)
        self.page = kwargs.get('page', None)


class FormFieldsReport(msrest.serialization.Model):
    """Report for a custom model training field.

    All required parameters must be populated in order to send to Azure.

    :param field_name: Required. Training field name.
    :type field_name: str
    :param accuracy: Required. Estimated extraction accuracy for this field.
    :type accuracy: float
    """

    _validation = {
        'field_name': {'required': True},
        'accuracy': {'required': True},
    }

    _attribute_map = {
        'field_name': {'key': 'fieldName', 'type': 'str'},
        'accuracy': {'key': 'accuracy', 'type': 'float'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(FormFieldsReport, self).__init__(**kwargs)
        self.field_name = kwargs.get('field_name', None)
        self.accuracy = kwargs.get('accuracy', None)


class KeysResult(msrest.serialization.Model):
    """Keys extracted by the custom model.

    All required parameters must be populated in order to send to Azure.

    :param clusters: Required. Object mapping clusterIds to a list of keys.
    :type clusters: dict[str, list[str]]
    """

    _validation = {
        'clusters': {'required': True},
    }

    _attribute_map = {
        'clusters': {'key': 'clusters', 'type': '{[str]}'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(KeysResult, self).__init__(**kwargs)
        self.clusters = kwargs.get('clusters', None)


class KeyValueElement(msrest.serialization.Model):
    """Information about the extracted key or value in a key-value pair.

    All required parameters must be populated in order to send to Azure.

    :param text: Required. The text content of the key or value.
    :type text: str
    :param bounding_box: Bounding box of the key or value.
    :type bounding_box: list[float]
    :param elements: When includeTextDetails is set to true, a list of references to the text
     elements constituting this key or value.
    :type elements: list[str]
    """

    _validation = {
        'text': {'required': True},
        'bounding_box': {'max_items': 8, 'min_items': 8},
    }

    _attribute_map = {
        'text': {'key': 'text', 'type': 'str'},
        'bounding_box': {'key': 'boundingBox', 'type': '[float]'},
        'elements': {'key': 'elements', 'type': '[str]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(KeyValueElement, self).__init__(**kwargs)
        self.text = kwargs.get('text', None)
        self.bounding_box = kwargs.get('bounding_box', None)
        self.elements = kwargs.get('elements', None)


class KeyValuePair(msrest.serialization.Model):
    """Information about the extracted key-value pair.

    All required parameters must be populated in order to send to Azure.

    :param label: A user defined label for the key/value pair entry.
    :type label: str
    :param key: Required. Information about the extracted key in a key-value pair.
    :type key: ~azure.ai.formrecognizer.models.KeyValueElement
    :param value: Required. Information about the extracted value in a key-value pair.
    :type value: ~azure.ai.formrecognizer.models.KeyValueElement
    :param confidence: Required. Confidence value.
    :type confidence: float
    """

    _validation = {
        'key': {'required': True},
        'value': {'required': True},
        'confidence': {'required': True, 'maximum': 1, 'minimum': 0},
    }

    _attribute_map = {
        'label': {'key': 'label', 'type': 'str'},
        'key': {'key': 'key', 'type': 'KeyValueElement'},
        'value': {'key': 'value', 'type': 'KeyValueElement'},
        'confidence': {'key': 'confidence', 'type': 'float'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(KeyValuePair, self).__init__(**kwargs)
        self.label = kwargs.get('label', None)
        self.key = kwargs.get('key', None)
        self.value = kwargs.get('value', None)
        self.confidence = kwargs.get('confidence', None)


class Model(msrest.serialization.Model):
    """Response to the get custom model operation.

    All required parameters must be populated in order to send to Azure.

    :param model_info: Required. Basic custom model information.
    :type model_info: ~azure.ai.formrecognizer.models.ModelInfo
    :param keys: Keys extracted by the custom model.
    :type keys: ~azure.ai.formrecognizer.models.KeysResult
    :param train_result: Custom model training result.
    :type train_result: ~azure.ai.formrecognizer.models.TrainResult
    """

    _validation = {
        'model_info': {'required': True},
    }

    _attribute_map = {
        'model_info': {'key': 'modelInfo', 'type': 'ModelInfo'},
        'keys': {'key': 'keys', 'type': 'KeysResult'},
        'train_result': {'key': 'trainResult', 'type': 'TrainResult'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Model, self).__init__(**kwargs)
        self.model_info = kwargs.get('model_info', None)
        self.keys = kwargs.get('keys', None)
        self.train_result = kwargs.get('train_result', None)


class ModelInfo(msrest.serialization.Model):
    """Basic custom model information.

    All required parameters must be populated in order to send to Azure.

    :param model_id: Required. Model identifier.
    :type model_id: str
    :param status: Required. Status of the model. Possible values include: 'creating', 'ready',
     'invalid'.
    :type status: str or ~azure.ai.formrecognizer.models.ModelStatus
    :param created_date_time: Required. Date and time (UTC) when the model was created.
    :type created_date_time: ~datetime.datetime
    :param last_updated_date_time: Required. Date and time (UTC) when the status was last updated.
    :type last_updated_date_time: ~datetime.datetime
    """

    _validation = {
        'model_id': {'required': True},
        'status': {'required': True},
        'created_date_time': {'required': True},
        'last_updated_date_time': {'required': True},
    }

    _attribute_map = {
        'model_id': {'key': 'modelId', 'type': 'str'},
        'status': {'key': 'status', 'type': 'str'},
        'created_date_time': {'key': 'createdDateTime', 'type': 'iso-8601'},
        'last_updated_date_time': {'key': 'lastUpdatedDateTime', 'type': 'iso-8601'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ModelInfo, self).__init__(**kwargs)
        self.model_id = kwargs.get('model_id', None)
        self.status = kwargs.get('status', None)
        self.created_date_time = kwargs.get('created_date_time', None)
        self.last_updated_date_time = kwargs.get('last_updated_date_time', None)


class Models(msrest.serialization.Model):
    """Response to the list custom models operation.

    :param summary: Summary of all trained custom models.
    :type summary: ~azure.ai.formrecognizer.models.ModelsSummary
    :param model_list: Collection of trained custom models.
    :type model_list: list[~azure.ai.formrecognizer.models.ModelInfo]
    :param next_link: Link to the next page of custom models.
    :type next_link: str
    """

    _attribute_map = {
        'summary': {'key': 'summary', 'type': 'ModelsSummary'},
        'model_list': {'key': 'modelList', 'type': '[ModelInfo]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Models, self).__init__(**kwargs)
        self.summary = kwargs.get('summary', None)
        self.model_list = kwargs.get('model_list', None)
        self.next_link = kwargs.get('next_link', None)


class ModelsSummary(msrest.serialization.Model):
    """Summary of all trained custom models.

    All required parameters must be populated in order to send to Azure.

    :param count: Required. Current count of trained custom models.
    :type count: int
    :param limit: Required. Max number of models that can be trained for this account.
    :type limit: int
    :param last_updated_date_time: Required. Date and time (UTC) when the summary was last updated.
    :type last_updated_date_time: ~datetime.datetime
    """

    _validation = {
        'count': {'required': True},
        'limit': {'required': True},
        'last_updated_date_time': {'required': True},
    }

    _attribute_map = {
        'count': {'key': 'count', 'type': 'int'},
        'limit': {'key': 'limit', 'type': 'int'},
        'last_updated_date_time': {'key': 'lastUpdatedDateTime', 'type': 'iso-8601'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ModelsSummary, self).__init__(**kwargs)
        self.count = kwargs.get('count', None)
        self.limit = kwargs.get('limit', None)
        self.last_updated_date_time = kwargs.get('last_updated_date_time', None)


class PageResult(msrest.serialization.Model):
    """Extracted information from a single page.

    All required parameters must be populated in order to send to Azure.

    :param page: Required. Page number.
    :type page: int
    :param cluster_id: Cluster identifier.
    :type cluster_id: int
    :param key_value_pairs: List of key-value pairs extracted from the page.
    :type key_value_pairs: list[~azure.ai.formrecognizer.models.KeyValuePair]
    :param tables: List of data tables extracted from the page.
    :type tables: list[~azure.ai.formrecognizer.models.DataTable]
    """

    _validation = {
        'page': {'required': True, 'minimum': 1},
        'cluster_id': {'minimum': 0},
    }

    _attribute_map = {
        'page': {'key': 'page', 'type': 'int'},
        'cluster_id': {'key': 'clusterId', 'type': 'int'},
        'key_value_pairs': {'key': 'keyValuePairs', 'type': '[KeyValuePair]'},
        'tables': {'key': 'tables', 'type': '[DataTable]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(PageResult, self).__init__(**kwargs)
        self.page = kwargs.get('page', None)
        self.cluster_id = kwargs.get('cluster_id', None)
        self.key_value_pairs = kwargs.get('key_value_pairs', None)
        self.tables = kwargs.get('tables', None)


class ReadResult(msrest.serialization.Model):
    """Text extracted from a page in the input document.

    All required parameters must be populated in order to send to Azure.

    :param page: Required. The 1-based page number in the input document.
    :type page: int
    :param angle: Required. The general orientation of the text in clockwise direction, measured in
     degrees between (-180, 180].
    :type angle: float
    :param width: Required. The width of the image/PDF in pixels/inches, respectively.
    :type width: float
    :param height: Required. The height of the image/PDF in pixels/inches, respectively.
    :type height: float
    :param unit: Required. The unit used by the width, height and boundingBox properties. For
     images, the unit is "pixel". For PDF, the unit is "inch". Possible values include: 'pixel',
     'inch'.
    :type unit: str or ~azure.ai.formrecognizer.models.LengthUnit
    :param language: The detected language on the page overall. Possible values include: 'en',
     'es'.
    :type language: str or ~azure.ai.formrecognizer.models.Language
    :param lines: When includeTextDetails is set to true, a list of recognized text lines. The
     maximum number of lines returned is 300 per page. The lines are sorted top to bottom, left to
     right, although in certain cases proximity is treated with higher priority. As the sorting
     order depends on the detected text, it may change across images and OCR version updates. Thus,
     business logic should be built upon the actual line location instead of order.
    :type lines: list[~azure.ai.formrecognizer.models.TextLine]
    """

    _validation = {
        'page': {'required': True, 'minimum': 1},
        'angle': {'required': True, 'maximum': 180, 'minimum_ex': -180},
        'width': {'required': True, 'minimum': 0},
        'height': {'required': True, 'minimum': 0},
        'unit': {'required': True},
    }

    _attribute_map = {
        'page': {'key': 'page', 'type': 'int'},
        'angle': {'key': 'angle', 'type': 'float'},
        'width': {'key': 'width', 'type': 'float'},
        'height': {'key': 'height', 'type': 'float'},
        'unit': {'key': 'unit', 'type': 'str'},
        'language': {'key': 'language', 'type': 'str'},
        'lines': {'key': 'lines', 'type': '[TextLine]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ReadResult, self).__init__(**kwargs)
        self.page = kwargs.get('page', None)
        self.angle = kwargs.get('angle', None)
        self.width = kwargs.get('width', None)
        self.height = kwargs.get('height', None)
        self.unit = kwargs.get('unit', None)
        self.language = kwargs.get('language', None)
        self.lines = kwargs.get('lines', None)


class SourcePath(msrest.serialization.Model):
    """Uri or local path to source data.

    :param source: File source path.
    :type source: str
    """

    _validation = {
        'source': {'max_length': 2048, 'min_length': 0},
    }

    _attribute_map = {
        'source': {'key': 'source', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(SourcePath, self).__init__(**kwargs)
        self.source = kwargs.get('source', None)


class TextLine(msrest.serialization.Model):
    """An object representing an extracted text line.

    All required parameters must be populated in order to send to Azure.

    :param text: Required. The text content of the line.
    :type text: str
    :param bounding_box: Required. Bounding box of an extracted line.
    :type bounding_box: list[float]
    :param language: The detected language of this line, if different from the overall page
     language. Possible values include: 'en', 'es'.
    :type language: str or ~azure.ai.formrecognizer.models.Language
    :param words: Required. List of words in the text line.
    :type words: list[~azure.ai.formrecognizer.models.TextWord]
    """

    _validation = {
        'text': {'required': True},
        'bounding_box': {'required': True, 'max_items': 8, 'min_items': 8},
        'words': {'required': True},
    }

    _attribute_map = {
        'text': {'key': 'text', 'type': 'str'},
        'bounding_box': {'key': 'boundingBox', 'type': '[float]'},
        'language': {'key': 'language', 'type': 'str'},
        'words': {'key': 'words', 'type': '[TextWord]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(TextLine, self).__init__(**kwargs)
        self.text = kwargs.get('text', None)
        self.bounding_box = kwargs.get('bounding_box', None)
        self.language = kwargs.get('language', None)
        self.words = kwargs.get('words', None)


class TextWord(msrest.serialization.Model):
    """An object representing a word.

    All required parameters must be populated in order to send to Azure.

    :param text: Required. The text content of the word.
    :type text: str
    :param bounding_box: Required. Bounding box of an extracted word.
    :type bounding_box: list[float]
    :param confidence: Confidence value.
    :type confidence: float
    """

    _validation = {
        'text': {'required': True},
        'bounding_box': {'required': True, 'max_items': 8, 'min_items': 8},
        'confidence': {'maximum': 1, 'minimum': 0},
    }

    _attribute_map = {
        'text': {'key': 'text', 'type': 'str'},
        'bounding_box': {'key': 'boundingBox', 'type': '[float]'},
        'confidence': {'key': 'confidence', 'type': 'float'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(TextWord, self).__init__(**kwargs)
        self.text = kwargs.get('text', None)
        self.bounding_box = kwargs.get('bounding_box', None)
        self.confidence = kwargs.get('confidence', None)


class TrainingDocumentInfo(msrest.serialization.Model):
    """Report for a custom model training document.

    All required parameters must be populated in order to send to Azure.

    :param document_name: Required. Training document name.
    :type document_name: str
    :param pages: Required. Total number of pages trained.
    :type pages: int
    :param errors: Required. List of errors.
    :type errors: list[~azure.ai.formrecognizer.models.ErrorInformation]
    :param status: Required. Status of the training operation. Possible values include:
     'succeeded', 'partiallySucceeded', 'failed'.
    :type status: str or ~azure.ai.formrecognizer.models.TrainStatus
    """

    _validation = {
        'document_name': {'required': True},
        'pages': {'required': True},
        'errors': {'required': True},
        'status': {'required': True},
    }

    _attribute_map = {
        'document_name': {'key': 'documentName', 'type': 'str'},
        'pages': {'key': 'pages', 'type': 'int'},
        'errors': {'key': 'errors', 'type': '[ErrorInformation]'},
        'status': {'key': 'status', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(TrainingDocumentInfo, self).__init__(**kwargs)
        self.document_name = kwargs.get('document_name', None)
        self.pages = kwargs.get('pages', None)
        self.errors = kwargs.get('errors', None)
        self.status = kwargs.get('status', None)


class TrainRequest(msrest.serialization.Model):
    """Request parameter to train a new custom model.

    All required parameters must be populated in order to send to Azure.

    :param source: Required. Source path containing the training documents.
    :type source: str
    :param source_filter: Filter to apply to the documents in the source path for training.
    :type source_filter: ~azure.ai.formrecognizer.models.TrainSourceFilter
    :param use_label_file: Use label file for training a model.
    :type use_label_file: bool
    """

    _validation = {
        'source': {'required': True, 'max_length': 2048, 'min_length': 0},
    }

    _attribute_map = {
        'source': {'key': 'source', 'type': 'str'},
        'source_filter': {'key': 'sourceFilter', 'type': 'TrainSourceFilter'},
        'use_label_file': {'key': 'useLabelFile', 'type': 'bool'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(TrainRequest, self).__init__(**kwargs)
        self.source = kwargs.get('source', None)
        self.source_filter = kwargs.get('source_filter', None)
        self.use_label_file = kwargs.get('use_label_file', False)


class TrainResult(msrest.serialization.Model):
    """Custom model training result.

    All required parameters must be populated in order to send to Azure.

    :param training_documents: Required. List of the documents used to train the model and any
     errors reported in each document.
    :type training_documents: list[~azure.ai.formrecognizer.models.TrainingDocumentInfo]
    :param fields: List of fields used to train the model and the train operation error reported by
     each.
    :type fields: list[~azure.ai.formrecognizer.models.FormFieldsReport]
    :param average_model_accuracy: Average accuracy.
    :type average_model_accuracy: float
    :param errors: Errors returned during the training operation.
    :type errors: list[~azure.ai.formrecognizer.models.ErrorInformation]
    """

    _validation = {
        'training_documents': {'required': True},
    }

    _attribute_map = {
        'training_documents': {'key': 'trainingDocuments', 'type': '[TrainingDocumentInfo]'},
        'fields': {'key': 'fields', 'type': '[FormFieldsReport]'},
        'average_model_accuracy': {'key': 'averageModelAccuracy', 'type': 'float'},
        'errors': {'key': 'errors', 'type': '[ErrorInformation]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(TrainResult, self).__init__(**kwargs)
        self.training_documents = kwargs.get('training_documents', None)
        self.fields = kwargs.get('fields', None)
        self.average_model_accuracy = kwargs.get('average_model_accuracy', None)
        self.errors = kwargs.get('errors', None)


class TrainSourceFilter(msrest.serialization.Model):
    """Filter to apply to the documents in the source path for training.

    :param prefix: A case-sensitive prefix string to filter documents in the source path for
     training. For example, when using a Azure storage blob Uri, use the prefix to restrict sub
     folders for training.
    :type prefix: str
    :param include_sub_folders: A flag to indicate if sub folders within the set of prefix folders
     will also need to be included when searching for content to be preprocessed.
    :type include_sub_folders: bool
    """

    _validation = {
        'prefix': {'max_length': 1024, 'min_length': 0},
    }

    _attribute_map = {
        'prefix': {'key': 'prefix', 'type': 'str'},
        'include_sub_folders': {'key': 'includeSubFolders', 'type': 'bool'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(TrainSourceFilter, self).__init__(**kwargs)
        self.prefix = kwargs.get('prefix', None)
        self.include_sub_folders = kwargs.get('include_sub_folders', False)
