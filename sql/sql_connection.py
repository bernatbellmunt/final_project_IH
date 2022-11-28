import sqlalchemy as alch
import os
from dotenv import load_dotenv

load_dotenv()

dbName = "final_project"
password=os.getenv("sql_pass")


connectionData = f"mysql+pymysql://root:{password}@localhost/{dbName}"
engine = alch.create_engine(connectionData)