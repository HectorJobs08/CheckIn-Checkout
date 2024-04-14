from fastapi import FastAPI

from src.routes.EmployeesRoutes import employees_router
from src.routes.RecordRoutes import record_router

app = FastAPI()

app.include_router(employees_router)
app.include_router(record_router)

@app.get('/')
def root():
    return { "hello": "world" }