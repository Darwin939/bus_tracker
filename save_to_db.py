import psycopg2
conn = psycopg2.connect(dbname='root', user='root', 
                        password='secret', host='localhost')
cursor = conn.cursor()

cursor.execute('select now()')
a = cursor.fetchone()
print(a)