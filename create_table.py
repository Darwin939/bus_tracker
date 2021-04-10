import psycopg2

conn = psycopg2.connect(dbname='postgres', user='postgres', 
                        password='secret', host='localhost')
cursor = conn.cursor()
cursor.execute(open("./queries/create.sql",'r').read())
conn.commit()