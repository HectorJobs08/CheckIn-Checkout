from fastapi import APIRouter

from src.models.RecordModel import Record

from src.controllers.RecordController import records_by_user
from src.controllers.RecordController import store

record_router = APIRouter()

@record_router.get('/records/{id}')
def get_records_by_user(id: str):
    return records_by_user(id)

@record_router.post('/records/store')
def store_record(record: Record):
    return store(record)