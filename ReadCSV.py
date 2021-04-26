
import csv
import datetime

day = datetime.datetime.strptime(input("Type Date yyyy-mm-dd: "), "%Y-%m-%d")

data = []

def getstuff(filename, day):
    with open(filename, "r") as csvfile:
        datareader = csv.reader(csvfile, delimiter=',')
        next(datareader, None)
        for row in datareader:
            if (datetime.datetime.strptime(row[0][:-16] , "%Y-%m-%d") == day) and (row[4] == "false"):  
                yield row[2], int(row[3])

for iter in getstuff("test.csv", day):
    data.append(iter)

categories = set(map(lambda x:x[0], data))
final = []

#The main question - how to improve this?
for cat in categories:
    sm = 0
    for row in data:
        if row[0] == cat:
            sm+=row[1]
    obj = [cat, sm]
    final.append(obj)

final.sort()

print(final)
