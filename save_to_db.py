import psycopg2
import csv
from datetime import datetime
from queries import queries 

bus_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,
               18, 19, 20, 21, 22, 23, 24, 25, 28, 29, 31, 32, 34, 35, 36,
               37, 39, 40, 41, 44, 46, 47, 48, 50, 51, 52, 53, 54, 56, 60,
               61, 64, 70, 71, 72, 73, 80, 81, 120]

conn = psycopg2.connect(dbname='postgres', user='postgres', 
                        password='secret', host='localhost')
cursor = conn.cursor()
cursor.execute(open("./queries/create.sql",'r').read())
conn.commit()

bus_data_path = "./bus/bus/bus_"

#insert bus data to db
def insert_row_to_db(row):
    insert_query = """ INSERT INTO bus (bus_id,route_number,time_at, iteration, pt)
                              VALUES (%s, %s, %s, %s, ST_GeomFromText(%s, 4326))"""
    date_time_obj = datetime.strptime(row[2],'%Y-%m-%d %H:%M:%S')
    point = "POINT({} {})".format(row[4],row[3])
    item_tuple = (row[0],row[1],date_time_obj,row[6],point)
    cursor.execute(insert_query, item_tuple)
    conn.commit()

#csv contain 7 columns
def insert_bus_to_db(path):
    with open(path) as file:
        file = csv.reader(file,delimiter = ',')
        for row in file:
            insert_row_to_db(row)

def save_bus_to_db():
    for bus in bus_numbers:
        path = bus_data_path + str(bus)+".csv"
        insert_bus_to_db(path)

def insert_bus_stop_row_to_db(row):
    insert_query = """ INSERT INTO bus_stop (pt)
                              VALUES (ST_GeomFromText(%s, 4326))"""
    point = "POINT({} {})".format(row[1],row[2])
    item_tuple = (point,)
    cursor.execute(insert_query, item_tuple)
    conn.commit()

def insert_bus_stop_to_db():
    with open("./bus/bus_stops/bus_stops.csv") as file:
        file = csv.reader(file,delimiter = ',')
        for row in file:
            insert_bus_stop_row_to_db(row)

def get_buses_per_iteration(iteration ):
    query = queries.getBusesLiedOnBusStopBuffer
    cursor.execute(query, (iteration,))
    records = cursor.fetchall()
    return records

def update_bus_stop_latest_id(row):
    query = queries.updateLatestBusStopId
    cursor.execute(query, (row[-3],row[0]))
    conn.commit()

def set_delay_time(time,bus_id,bus_stop_id):
    query = queries.setDelayHistoryForBus
    cursor.execute(query, (time,bus_id,bus_stop_id))
    conn.commit()

def calculate_delay_for_bus(iteration):
    buses = get_buses_per_iteration(iteration)
    for bus in buses:
        update_bus_stop_latest_id(bus)
        set_delay_time(bus[5],bus[0],bus[-3])

# не интеджер а его айди(который стирнг) и скорее всего уменьшить буфер
# через его id можно вытягивать его uniq

if __name__ == "__main__":
    # save_bus_to_db()
    # insert_bus_stop_to_db()
    # for i in range(732):
    #     calculate_delay_for_bus(i)