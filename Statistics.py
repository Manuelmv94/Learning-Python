print ("This program will store 10 values in a list and then return some statistic info")

import statistics

numbers=[]
t=0
for i in range(10):
    n=i+1
    x=float(input("Please enter the value number %s of the list: " %n))
    numbers.append(x)
s=sum(numbers)
a=statistics.mean(numbers)
st=statistics.stdev(numbers)
print ("The total of the numbers is:%s" %s)
print ("The average of the numbers is:%s" %a)
print ("The standard deviation is:%s" %st)
