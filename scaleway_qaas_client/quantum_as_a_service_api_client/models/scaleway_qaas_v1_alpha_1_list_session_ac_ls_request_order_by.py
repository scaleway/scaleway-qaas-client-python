from enum import Enum


class ScalewayQaasV1Alpha1ListSessionACLsRequestOrderBy(str, Enum):
    ACCESS_ASC = "access_asc"
    ACCESS_DESC = "access_desc"

    def __str__(self) -> str:
        return str(self.value)
