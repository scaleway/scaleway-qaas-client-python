from enum import Enum


class ScalewayQaasV1Alpha1SessionOriginType(str, Enum):
    CUSTOMER = "customer"
    PROCESS = "process"
    UNKNOWN_ORIGIN_TYPE = "unknown_origin_type"

    def __str__(self) -> str:
        return str(self.value)
