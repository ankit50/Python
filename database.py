import psycopg2
conn = psycopg2.connect(dbname="Console Games", user="postgres", password="root")
cur = conn.cursor()
cur.execute("SELECT *FROM console_dates")
for row, a, d, f, fe in cur:
    print(row)
    print(a)
    print(d)
    print(f)
    print(fe)
    print("********************************")
cur.close()
conn.close()
