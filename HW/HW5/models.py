from typing import Optional
from pydantic import BaseModel


class Task(BaseModel):
    name: str
    description: Optional[str] = None
    complete_status: bool = False
