"""
API 서버의 설정 파일
"""

import pandas as pd
from sqlalchemy import create_engine

BASE_URL = "http://localhost"
PORT = 5000

DB_HOST = "localhost"
DB_PORT = 3306
DB_USER = "root"
DB_PASSWORD = "1234"
DB_NAME = 'kakaotalk'