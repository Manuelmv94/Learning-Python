print ("This program will store some values in a list and then return some statistic info")

numbers=[]
r="y"
n=1
t=0
while r=="y":
    x=float(input("Please enter the value number %s of the list: " %n))
    numbers.append(x)

    t=t+x
    r=input("Do you want to add another element to the list? (y/n)")
    while r !="y" and r!="n":
        r=input("%s is not an option, Please try again (y/n): " %(r))
    if r=="y":
        n=n+1

a=t/n
sm=0
for i in numbers:
    su=(i - a)**2
    sm=sm+su
sd=(sm/(n-1))**(0.5)


print ("The total of the numbers is:%s" %t)
print ("The average of the numbers is:%s" %a)
print ("The standard deviation is:%s" %sd)
