import mysql.connector
from mysql.connector import pooling,Error

class MySqlDatabase:
    def __init__(self, host, user, password, database, pool_size=5):
        self.config = {
            'host': host,
            'user': user,
            'password': password,
            'database': database,
            'autocommit': False
        }
        self.pool = pooling.MySQLConnectionPool(pool_name="mypool",
                                                pool_size=pool_size,
                                                pool_reset_session=True,
                                                **self.config)
    
    def execute_query(self, query, params = None, fetch = True):
        conn = None
        cursor = None
        try:
            conn = self.pool.get_connection()
            cursor = conn.cursor(dictionary=True, buffered=True)
            cursor.execute(query, params)
            conn.commit()
            return cursor.fetchall() if fetch else None
        except Error as e:
            if conn:
                conn.rollback()
            print(f"Error en consulta: {e}")
            return None
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()