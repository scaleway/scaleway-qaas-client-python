from enum import Enum


class ScalewayQaasV1Alpha1PlatformType(str, Enum):
    QPU = "qpu"
    SIMULATOR = "simulator"
    UNKNOWN_TYPE = "unknown_type"

    def __str__(self) -> str:
        return str(self.value)
