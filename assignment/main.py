from fastapi import FastAPI

from employee_service import get_employee_details, get_employee_details_count
from model import EmployeeQuery

app = FastAPI()

@app.post("/employee")
def employees_report(employee_query : EmployeeQuery):
    return {"total_count":get_employee_details_count(employee_query),"data":get_employee_details(employee_query)}