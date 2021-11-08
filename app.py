import csv
import math

with open("data.csv",newline ="") as f:
    r = csv.reader(f)
    data = list(r)

list = []
for i in range(len(data)):
    num = data[i][0]
    list.append(float(num))

number_in_list = len(list)
total = 0
for i in list:
    total += i

mean = total / number_in_list
print("Mean is : ",mean)

list1 = []

for i in list:
    a = int(i)-int(mean)
    b=a*a
    list1.append(b)

c=0

for i in list1:
    c = c+i

c=c/(number_in_list-1)
c = math.sqrt(c)

print(c)