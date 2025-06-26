from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql://bircham_test_db_user:oR1OpAV8VemzojRnrXPqZcFGx2o7cg4s@dpg-d1eliqvgi27c73epi0l0-a.oregon-postgres.render.com/bircham_test_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()
