from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# Record Types
# 0: out of office
# 1: Working
# 2: Lunch

class Record(BaseModel):
    user_id: str
    record_type: int
    created_at: Optional[datetime] = datetime.now()
