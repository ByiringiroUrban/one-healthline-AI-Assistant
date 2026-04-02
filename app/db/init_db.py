from app.db.base import Base
from app.db.session import engine

# import models here
from app.models import patient

def init_db():
    Base.metadata.create_all(bind=engine)