import psycopg2
import psycopg2.extras as ext
import os

DATABASE_URL = os.environ.get('DATABASE_URL')

def run_sql(sql, values = None):
    results = []
    conn = None
    try:
        # gym_manager
        # conn = psycopg2.connect("dbname='postgresql-animate-23710'")
        conn = psycopg2.connect(DATABASE_URL, sslmode='require')
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute(sql, values)
        conn.commit()
        results = cur.fetchall()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return results
