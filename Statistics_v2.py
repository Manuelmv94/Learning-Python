print ("This program will store some values in a list and then return some statistic info")

import statistics

numbers=[]
r="y"
n=1
while r=="y":
    x=float(input("Please enter the value number %s of the list: " %n))
    numbers.append(x)
    n=n+1
    r=input("Do you want to add another element to the list? (y/n)")
    while r !="y" and r!="n":
        r=input("%s is not an option, Please try again (y/n): " %(r))

s=sum(numbers)
a=statistics.mean(numbers)
st=statistics.stdev(numbers)
print ("The total of the numbers is:%s" %s)
print ("The average of the numbers is:%s" %a)
print ("The standard deviation is:%s" %st)
