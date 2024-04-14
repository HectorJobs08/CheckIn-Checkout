from fastapi import APIRouter

# Models
from src.models.EmployeeModel import Employee

# Controllers
from src.controllers.EmployeesController import index
from src.controllers.EmployeesController import query
from src.controllers.EmployeesController import store
from src.controllers.EmployeesController import destroy

employees_router = APIRouter()

@employees_router.get('/employees')
def get_employees():
    return index()

@employees_router.get('/employee/{id}')
def get_employee_by_id(id: str):
    return query(id)

@employees_router.post('/employees/store')
def store_employee(employee: Employee):
    return store(employee)

@employees_router.delete('/employees/destroy/{id}')
def delete_employee(id: str):
    return destroy(id)