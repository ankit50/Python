import psycopg2
conn = psycopg2.connect(dbname="Console Games", user="postgres", password="root")
cur = conn.cursor()
cur.execute("SELECT *FROM console_games")
records = cur.fetchall()
for


cur.close()
conn.close()
