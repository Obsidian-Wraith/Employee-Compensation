from database.models import EmployeeData, EmployeeRating, AverageIndustryCompensation
from sqlalchemy import text

def fetch_all_employee_data(db):
    records = db.query(EmployeeData).all()
    return [r.as_dict() for r in records]

def fetch_all_employee_rating(db):
    records = db.query(EmployeeRating).all()
    return [r.as_dict() for r in records]

def fetch_all_industry_compensation(db):
    records = db.query(AverageIndustryCompensation).all()
    return [r.as_dict() for r in records]

def fetch_filtered_employee_data(db, role_filter=None, include_inactive=False, selected_location=None):
    query = db.query(EmployeeData)

    if role_filter:
        query = query.filter(EmployeeData.role == role_filter)
    if not include_inactive:
        query = query.filter(EmployeeData.active == True)
    if selected_location:
        query = query.filter(EmployeeData.location == selected_location)

    records = query.all()
    return [r.as_dict() for r in records]


def fetch_experience_distribution(db, selected_location=None, selected_role=None):
    query = db.query(EmployeeData)

    if selected_location:
        query = query.filter(EmployeeData.location == selected_location)
    if selected_role:
        query = query.filter(EmployeeData.role == selected_role)

    records = query.all()

    # Define ranges
    buckets = {
        '0-1': 0,
        '1-2': 0,
        '2-5': 0,
        '5-10': 0,
        '10+': 0
    }

    for r in records:
        exp = r.years_of_experience
        if exp < 1:
            buckets['0-1'] += 1
        elif exp < 2:
            buckets['1-2'] += 1
        elif exp < 5:
            buckets['2-5'] += 1
        elif exp < 10:
            buckets['5-10'] += 1
        else:
            buckets['10+'] += 1

    # Return as list of dicts
    return [{"experience_range": k, "employee_count": v} for k, v in buckets.items()]
