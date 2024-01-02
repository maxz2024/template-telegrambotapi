from pathlib import Path
from sqlalchemy import create_engine

from utils.db_api.home_db.models import user

engine = create_engine(f'sqlite:///{Path("files/home.db")}')

user.Base.metadata.create_all(engine)