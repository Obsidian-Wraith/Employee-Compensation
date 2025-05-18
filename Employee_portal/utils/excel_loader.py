import pandas as pd
from utils import normalize
from database import models

def insert_data_from_excel(table_name, df, db):
    if table_name == 'employee_data':
        df['Years of Experience'] = df['Years of Experience'].apply(normalize.normalize_yoe)
        df['Active'] = df['Active'].apply(normalize.normalize_active)
        # df['Last Working Day'] = normalize.normalize_last_working_day(df['Last Working Day'])

        for _, row in df.iterrows():
            record = models.EmployeeData(
                name=row['Name'],
                role=row['Role'],
                location=row['Location'],
                years_of_experience=row['Years of Experience'],
                active=row['Active'],
                current_comp=row['Current Comp (INR)'],
                last_working_day=normalize.normalize_last_working_day(row['Last Working Day'])
            )
            print(record.last_working_day)
            db.merge(record)

    elif table_name == 'average_industry_compensation':
        for _, row in df.iterrows():
            record = models.AverageIndustryCompensation(
                location=row['Location'],
                role=row['Role'],
                average_industry_compensation=row['Average Industry Compensation']
            )
            db.merge(record)

    elif table_name == 'employee_rating':
        df['Years of Experience'] = df['Years of Experience'].apply(normalize.normalize_yoe)

        print('after normalization')
        for _, row in df.iterrows():
            record = models.EmployeeRating(
                name=row['Name'],
                role=row['Role'],
                location=row['Location'],
                years_of_experience=row['Years of Experience'],
                l3q_self_rating=row['L3Q Average Self Rating'],
                l3q_manager_rating=row['L3Q Average Manager Rating']
            )
            print(record.years_of_experience)
            db.merge(record)

    else:
        raise ValueError("Invalid table name")

    db.commit()
