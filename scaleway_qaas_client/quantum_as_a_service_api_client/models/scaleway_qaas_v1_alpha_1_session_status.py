from enum import Enum


class ScalewayQaasV1Alpha1SessionStatus(str, Enum):
    RUNNING = "running"
    STARTING = "starting"
    STOPPED = "stopped"
    STOPPING = "stopping"
    UNKNOWN_STATUS = "unknown_status"

    def __str__(self) -> str:
        return str(self.value)
