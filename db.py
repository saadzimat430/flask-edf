import psycopg2
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

conn = psycopg2.connect(host="localhost",
                        user="postgres",
                        password="root",
                        database="postgres",
                        options="-c search_path=market-rates,public")

cur = conn.cursor()

cur.execute('TRUNCATE TABLE price')

copy_sql = """
           COPY price FROM stdin WITH CSV HEADER
           DELIMITER as ','
           """

with open('static/market.csv', 'r') as f:
    cur.copy_expert(sql=copy_sql, file=f)
    print("successfully imported csv to database")
    conn.commit()
    cur.close()
