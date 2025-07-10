from enum import Enum


class ScalewayQaasV1Alpha1PlatformTechnology(str, Enum):
    GENERAL_PURPOSE = "general_purpose"
    NEUTRAL_ATOM = "neutral_atom"
    PHOTONIC = "photonic"
    SUPERCONDUCTING = "superconducting"
    TRAPPED_ION = "trapped_ion"
    UNKNOWN_TECHNOLOGY = "unknown_technology"

    def __str__(self) -> str:
        return str(self.value)
