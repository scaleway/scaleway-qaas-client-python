from enum import Enum


class ListBookingsOrderBy(str, Enum):
    CREATED_AT_ASC = "created_at_asc"
    CREATED_AT_DESC = "created_at_desc"
    STARTED_AT_ASC = "started_at_asc"
    STARTED_AT_DESC = "started_at_desc"

    def __str__(self) -> str:
        return str(self.value)
