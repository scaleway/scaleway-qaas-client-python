from enum import Enum


class ScalewayQaasV1Alpha1SessionAccess(str, Enum):
    FULL = "full"
    READ_JOB = "read_job"
    READ_JOB_CIRCUIT = "read_job_circuit"
    READ_JOB_RESULT = "read_job_result"
    READ_SESSION = "read_session"
    READ_WRITE_JOB = "read_write_job"
    READ_WRITE_SESSION = "read_write_session"
    UNKNOWN_ACCESS = "unknown_access"

    def __str__(self) -> str:
        return str(self.value)
