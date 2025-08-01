from enum import Enum


class ListPlatformsOrderBy(str, Enum):
    BACKEND_NAME_ASC = "backend_name_asc"
    BACKEND_NAME_DESC = "backend_name_desc"
    NAME_ASC = "name_asc"
    NAME_DESC = "name_desc"
    PROVIDER_NAME_ASC = "provider_name_asc"
    PROVIDER_NAME_DESC = "provider_name_desc"
    TECHNOLOGY_ASC = "technology_asc"
    TECHNOLOGY_DESC = "technology_desc"
    TYPE_ASC = "type_asc"
    TYPE_DESC = "type_desc"

    def __str__(self) -> str:
        return str(self.value)
