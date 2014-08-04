"""Add headers to the CSV-file to make SQL import easier"""
import csv

with open('processed_data/rc13.csv', 'r') as csv_in:
    reader = csv.reader(csv_in, delimiter=";")
     line = reader.next()
     col_num = len(line)

lhead = []
for n in range(0, col_num):
    num = n + 1
    shead = 'col'+str(num)
    lhead.append(shead)

with open('processed_data/rc13.csv', 'wb') as csv_out:
    writer = csv.DictWriter(csv_out, fieldnames=lhead, delimiter=';')
    writer.writeheader()
