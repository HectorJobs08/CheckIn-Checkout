from fastapi import FastAPI

from src.routes.EmployeesRoutes import employees_router

app = FastAPI()

app.include_router(employees_router)

@app.get('/')
def root():
    return { "hello": "world" }