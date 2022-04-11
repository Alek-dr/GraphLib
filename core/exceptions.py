class EdgeOperationError(Exception):
    pass


class EdgeAddError(EdgeOperationError):
    pass


class EdgeRemoveError(EdgeOperationError):
    pass


class VertexException(Exception):
    pass


class VertexNotFound(VertexException):
    pass
