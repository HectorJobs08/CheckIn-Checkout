from bson import ObjectId

# Config
from src.config.mongo import employees_collection

# Models
from src.models.EmployeeModel import Employee

# Utils
from src.utils.json_utils import get_items, get_item

def index():
    employees = get_items(employees_collection.find())
    return employees

def query(id: str):
    employee = get_item(employees_collection.find_one({ "_id": ObjectId(id) }))
    return employee

def store(employee: Employee):
    data = employee.model_dump()
    result = employees_collection.insert_one(data)
    employee = query(str(result.inserted_id))
    return employee


def destroy(id: str):
    result = employees_collection.delete_one({"_id": ObjectId(id)})
    return {"result": result, "status": True}