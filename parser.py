import requests
import time
import json
import csv
from datetime import datetime

BUS_COORDINATE_API = "http://45.135.131.226/api/buscoordinates/"
bus_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,
               18, 19, 20, 21, 22, 23, 24, 25, 28, 29, 31, 32, 34, 35, 36,
               37, 39, 40, 41, 44, 46, 47, 48, 50, 51, 52, 53, 54, 56, 60,
               61, 64, 70, 71, 72, 73, 80, 81, 120]
headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}

iteration = 1


def parser(iter, bus_number):
    url = BUS_COORDINATE_API+str(bus_number)
    r = requests.get(url, headers=headers)
    bus_dict = json.loads(r.text)
    bus_list = []

    for key in bus_dict:
        x = {"bus_id": key, 'iter': iter}
        z = {**bus_dict[key], **x}
        bus_list.append(z)

    save_to_json(bus_list, bus_number)


def save_to_json(bus_list, bus_number):
    filename = 'bus/'+'bus_' + str(bus_number) + ".csv"

    with open(filename, 'a+') as outfile:
        fieldnames = ['bus_id', 'route', 'time',
                      'latitude', 'longitude', 'angle', 'iter']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        for bus in bus_list:
            writer.writerow(bus)


def main():
    try:
        global iteration
        for bus in bus_numbers:
            parser(iteration, bus)
        iteration += 1
    except:
        print("Some problems with connection", datetime.now())


if __name__ == "__main__":

    while True:
        main()
        time.sleep(60)
