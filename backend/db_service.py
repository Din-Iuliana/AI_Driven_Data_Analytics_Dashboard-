import os
import psycopg2

def get_connection():
    """Create and return a connection to PostgreSQL."""
    return psycopg2.connect(os.getenv("DATABASE_URL"))

def execute_query(sql):
    """Execute a SQL query and return the results as a list of dictionaries."""
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