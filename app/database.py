from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from .config import settings

                                     # username:password@ipaddres/hostname/databasename    
                                     # 'postgresql://postgres:Lcr98895674@localhost:5432/fastapi' #
SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'
engine = create_engine(SQLALCHEMY_DATABASE_URL)

Sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = Sessionlocal()
    try:
        yield db 
    finally:
        db.close()

#while True:
#    try:
#        conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', password='Lcr98895674',cursor_factory=RealDictCursor)
#        
#        cursor = conn.cursor()
#        print("Database connection was succesfull")
#        break
#    except Exception as error:
#        print("Connecting to database failed")
#        print("Error: ", error)
#        time.sleep(5) 
