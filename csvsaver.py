import csv
import datetime as dt

def sensor_write(S):
  with open ('Readings/___.csv', 'a') as log:
        log_writer = csv.writer(log)
        log_writer.writerow({S})

file = open("Readings/___.csv", "r+")
file.truncate
file.close

start = dt.datetime.now()
while (dt.datetime.now() - start).seconds < 10:
    sensor_write(temp)
