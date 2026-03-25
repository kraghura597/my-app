from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False

class Task(TaskCreate):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
