from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# Status Types
# 0: Out of office
# 1: Working
# 2: Lunch

class Employee(BaseModel):
    name: str
    status: Optional[int] = 0
    created_at: Optional[datetime] = datetime.now()
