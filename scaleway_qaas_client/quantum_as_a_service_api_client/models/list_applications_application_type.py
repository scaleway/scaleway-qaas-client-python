from enum import Enum


class ListApplicationsApplicationType(str, Enum):
    UNKNOWN_TYPE = "unknown_type"
    VQE = "vqe"

    def __str__(self) -> str:
        return str(self.value)
