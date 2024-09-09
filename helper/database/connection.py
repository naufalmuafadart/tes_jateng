import pymysql
import os
from dotenv import load_dotenv

load_dotenv()

def get():
    conn = pymysql.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER_NAME'),
        password=os.getenv('DB_PASSWORD'),
        db=os.getenv('DB_DATABASE'),
    )
    return conn
