from enum import Enum


class ListJobsOrderBy(str, Enum):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"
    PLATFORM_NAME_ASC = "platform_name_asc"
    PLATFORM_NAME_DESC = "platform_name_desc"
    SESSION_NAME_ASC = "session_name_asc"
    SESSION_NAME_DESC = "session_name_desc"
    STATUS_ASC = "status_asc"
    STATUS_DESC = "status_desc"

    def __str__(self) -> str:
        return str(self.value)
