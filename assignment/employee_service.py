import mysql.connector

from model import EmployeeQuery

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Singh@54321",
    database="mydb"
)

mycursor = mydb.cursor()


def get_employee_details(employee_query: EmployeeQuery):
    query = "select * from employee "
    if employee_query.search_term:
        query += " where (name = '" + employee_query.search_term + "') or (position = '" + employee_query.search_term + "') or (office = '" + employee_query.search_term + "') or (start_date='" + employee_query.search_term + "') or (salary='" + employee_query.search_term + "')"
        if employee_query.search_term.isnumeric():
            query += " or (age = " + employee_query.search_term + ")"
    if employee_query.sort_column:
        query += " order by " + employee_query.sort_column + " " + employee_query.sort_direction
    query += " limit " + str(employee_query.start) + "," + str(employee_query.size)
    print(query)
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    return myresult


def get_employee_details_count(employee_query: EmployeeQuery):
    query = "select count(*) from employee "
    if employee_query.search_term:
        query += " where (name = '" + employee_query.search_term + "') or (position = '" + employee_query.search_term + "') or (office = '" + employee_query.search_term + "') or (start_date='" + employee_query.search_term + "') or (salary='" + employee_query.search_term + "')"
        if employee_query.search_term.isnumeric():
            query += " or (age = " + employee_query.search_term + ")"
    print(query)
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    return myresult
