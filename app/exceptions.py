class UnsupportedException(Exception):
    pass


class UnsupportedModelException(UnsupportedException):
    pass


class UnsupportedPipelineException(UnsupportedException):
    pass


class UnsupportedSchedulerException(UnsupportedException):
    pass