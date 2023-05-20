from typing import Optional

from pydantic import BaseModel


class EmployeeQuery(BaseModel):
    start: int
    size: int
    search_term: Optional[str]
    sort_column: Optional[str]
    sort_direction: Optional[str]