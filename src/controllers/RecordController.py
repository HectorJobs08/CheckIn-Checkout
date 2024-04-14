from bson import ObjectId

# Config
from src.config.mongo import records_collection

# Models
from src.models.RecordModel import Record

# Utils
from src.utils.json_utils import get_items, get_item

def records_by_user(id: str):
    records = get_items(
        records_collection.find({ "user_id": id })
    )
    return records

def query(id: str):
    record = get_item(records_collection.find_one({ "_id": ObjectId(id) }))
    return record


def store(record: Record):
    data = record.model_dump()
    result = records_collection.insert_one(data)
    employee = query(str(result.inserted_id))
    return employee
