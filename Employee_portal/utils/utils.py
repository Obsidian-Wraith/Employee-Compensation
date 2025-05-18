import csv
from io import StringIO
from flask import Response
from database.models import EmployeeData, EmployeeRating, AverageIndustryCompensation

def generate_filtered_csv(db, location=None, role=None, min_exp=None, max_exp=None):
    query = db.query(EmployeeData)

    if location:
        query = query.filter(EmployeeData.location == location)
    if role:
        query = query.filter(EmployeeData.role == role)
    if min_exp:
        query = query.filter(EmployeeData.years_of_experience >= float(min_exp))
    if max_exp:
        query = query.filter(EmployeeData.years_of_experience <= float(max_exp))

    employees = query.all()

    output = StringIO()
    writer = csv.writer(output)
    writer.writerow(['Name', 'Role', 'Location', 'Experience', 'Compensation', 'Status'])

    for emp in employees:
        # Adjust for increment if present in rating table
        increment = (
            emp.rating.increment_amount if hasattr(emp, 'rating') and emp.rating and emp.rating.increment_amount
            else 0
        )
        final_comp = emp.current_comp + increment
        writer.writerow([
            emp.name,
            emp.role,
            emp.location,
            emp.years_of_experience,
            round(final_comp, 2),
            emp.status
        ])

    output.seek(0)
    return output