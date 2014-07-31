import csv

f = open('processed_data/rc13.csv', 'r')
reader = csv.reader(f, delimiter=";")
line = reader.next()
col_num = len(line)
lhead = []
for n in range(0, col_num):
    col_num = n + 1
    lhead.append('col'+str(col_num))

with open('processed_data/rc13.csv', 'wb') as f2:
    writer = csv.DictWriter(f2, fieldnames=lhead, delimiter=';')
    writer.writeheader()
