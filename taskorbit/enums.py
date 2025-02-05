from enum import StrEnum


class Commands(StrEnum):
    GET_STATUS = "GET_STATUS"
    CLOSING = "CLOSING"

    @classmethod
    def validate_key(cls, key):
        return hasattr(cls, key)


class TaskStatus(StrEnum):
    RUNNING = "RUNNING"
    UNKNOWN = "UNKNOWN"


class WorkerType(StrEnum):
    class_type = "class_type"
    function_type = "function_type"
