from enum import Enum


class ScalewayQaasV1Alpha1ApplicationType(str, Enum):
    UNKNOWN_TYPE = "unknown_type"
    VQE = "vqe"

    def __str__(self) -> str:
        return str(self.value)
