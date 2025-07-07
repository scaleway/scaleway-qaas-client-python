from enum import Enum


class ScalewayQaasV1Alpha1JobStatus(str, Enum):
    CANCELLED = "cancelled"
    CANCELLING = "cancelling"
    COMPLETED = "completed"
    ERROR = "error"
    RUNNING = "running"
    UNKNOWN_STATUS = "unknown_status"
    WAITING = "waiting"

    def __str__(self) -> str:
        return str(self.value)
