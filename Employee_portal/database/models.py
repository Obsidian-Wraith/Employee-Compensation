from sqlalchemy import Column, String, Integer, Float, Boolean
from sqlalchemy.orm import declarative_base

Base = declarative_base()

# class EmployeeData(Base):
#     __tablename__ = 'employee_data'
#     name = Column(String, primary_key=True)
#     role = Column(String)
#     location = Column(String)
#     years_of_experience = Column(Float)
#     active = Column(Boolean)
#     current_comp = Column(Integer)
#     last_working_day = Column(String)

class EmployeeData(Base):
    __tablename__ = "employee_data"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    role = Column(String)
    location = Column(String)
    years_of_experience = Column(Float)
    active = Column(Boolean)
    current_comp = Column(Float)
    last_working_day = Column(String)

    def as_dict(self):
        return {
            "name": self.name,
            "role": self.role,
            "location": self.location,
            "years_of_experience": self.years_of_experience,
            "active": self.active,
            "current_comp": self.current_comp,
            "last_working_day": self.last_working_day
        }

class AverageIndustryCompensation(Base):
    __tablename__ = 'average_industry_compensation'
    location = Column(String, primary_key=True)
    role = Column(String, primary_key=True)
    average_industry_compensation = Column(Integer)
    
    def as_dict(self):
        return {
            "location": self.location,
            "role": self.role,
            "average_industry_compensation": self.average_industry_compensation
        }

class EmployeeRating(Base):
    __tablename__ = 'employee_rating'
    name = Column(String, primary_key=True)
    role = Column(String)
    location = Column(String)
    years_of_experience = Column(Float)
    l3q_self_rating = Column(Float)
    l3q_manager_rating = Column(Float)

    def as_dict(self):
        return {
            "name": self.name,
            "role": self.role,
            "location": self.location,
            "years_of_experience": self.years_of_experience,
            "l3q_self_rating": self.l3q_self_rating,
            "l3q_manager_rating": self.l3q_manager_rating
        }
