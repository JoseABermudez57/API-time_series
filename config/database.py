# Description: Database configuration file
from sqlalchemy import create_engine, MetaData
from dotenv import load_dotenv
import os

load_dotenv(".env")

engine = create_engine(os.getenv('DATA_BASE_URL'))
meta = MetaData()
conn = engine.connect()
