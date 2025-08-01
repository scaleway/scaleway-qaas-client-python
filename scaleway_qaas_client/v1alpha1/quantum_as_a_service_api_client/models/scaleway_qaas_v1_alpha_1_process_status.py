from enum import Enum


class ScalewayQaasV1Alpha1ProcessStatus(str, Enum):
    CANCELLED = "cancelled"
    CANCELLING = "cancelling"
    COMPLETED = "completed"
    ERROR = "error"
    RUNNING = "running"
    STARTING = "starting"
    UNKNOWN_STATUS = "unknown_status"

    def __str__(self) -> str:
        return str(self.value)
