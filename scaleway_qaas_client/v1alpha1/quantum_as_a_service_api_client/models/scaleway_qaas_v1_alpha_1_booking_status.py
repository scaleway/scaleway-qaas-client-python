from enum import Enum


class ScalewayQaasV1Alpha1BookingStatus(str, Enum):
    CANCELLED = "cancelled"
    CANCELLING = "cancelling"
    ERROR = "error"
    UNKNOWN_STATUS = "unknown_status"
    VALIDATED = "validated"
    VALIDATING = "validating"
    WAITING = "waiting"

    def __str__(self) -> str:
        return str(self.value)
