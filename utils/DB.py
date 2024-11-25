import pymysql

from common.Config import *

class DB:
    def __init__(self):
        self.conn = pymysql.connect(
            host=DB_HOST,
            port=DB_PORT,
            user=DB_USER,
            password=DB_PASSWORD,
            db=DB_NAME,
            charset='utf8'
        )

    def __del__(self):
        self.conn.close()

    def execute(self, sql:str):
        with self.conn.cursor() as cur:
            if sql.lower().startswith('select'):
                cur.execute(sql)
                result = cur.fetchall()
                columns = [desc[0] for desc in cur.description]
                return pd.DataFrame(result, columns=columns)
            else:
                cur.execute(sql)
                self.conn.commit()
                return cur.rowcount