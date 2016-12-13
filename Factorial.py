def factorial(a):
    ans=a
    b=a
    for i in range (a-1):
        ans=ans*(b-1)
        b=b-1
    print ("The factorial of %s is %s.( %s!=%s )" %(a,ans,a,ans))


r= "y"
while r=="y":

    while True:
        try:
            x=int(input("Please enter a non-negative integer number: "))
            break
        except ValueError:
            print ("Oops! you didn't enter an integer number, Try again")

    while x<0:
        try:
            x=int(input("%s is a negative number, Please try again: " %(x)))
        except ValueError:
            print ("Oops! you didn't enter an integer number, Try again")
            while True:
                try:
                    x=int(input("Please enter a non-negative integer number: "))
                    break
                except ValueError:
                    print ("Oops! you didn't enter an integer number, Try again")


    if x==0:
        print("The factorial of 0 is 1. ( 0!=1 )")

    else:
        factorial(x)
    r=input("Would you like to try another number? (y/n): ")
    while r !="y" and r!="n":
        r=input("%s is not an option, Please try again (y/n): " %(r))
