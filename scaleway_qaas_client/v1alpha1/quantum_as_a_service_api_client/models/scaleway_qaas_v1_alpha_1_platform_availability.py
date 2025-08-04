from enum import Enum


class ScalewayQaasV1Alpha1PlatformAvailability(str, Enum):
    AVAILABLE = "available"
    MAINTENANCE = "maintenance"
    SCARCE = "scarce"
    SHORTAGE = "shortage"
    UNKNOWN_AVAILABILITY = "unknown_availability"

    def __str__(self) -> str:
        return str(self.value)
