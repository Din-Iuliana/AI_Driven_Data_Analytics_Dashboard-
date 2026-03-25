import os
import psycopg2

def get_connection():
    return psycopg2.connect(os.getenv("DATABASE_URL"))

def execute_query(sql):
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute(sql)
        columns = [desc[0] for desc in cur.description]
        rows = cur.fetchall()
        results = []
        for row in rows:
            results.append(dict(zip(columns, row)))
        return results
    finally:
        conn.close()