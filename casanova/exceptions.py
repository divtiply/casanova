# =============================================================================
# Casanova Exceptions
# =============================================================================
#


class CasanovaError(Exception):
    pass


class ColumnNumberMismatchError(CasanovaError):
    pass


class EmptyFileError(CasanovaError):
    pass


class MissingColumnError(CasanovaError):
    pass


class InvalidFileError(CasanovaError):
    pass
