from .models import Base
from .db import engine

def create_all_tables():
    Base.metadata.create_all(bind=engine)
