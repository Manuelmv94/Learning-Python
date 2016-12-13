def suma(a,b):
    print ("The sum of the two numbers is: %s" %(a+b))
def dif(a,b):
    print ("The difference of the two numbers is: %s" %(a-b))
def pro(a,b):
    print ("The product of the two numbers is: %s" %(a*b))
def div(a,b):
    print ("The integer based division of the two numbers is: %s" %(a//b))
def rem(a,b):
    print ("The remainder of the integer division is: %s" %(a%b))

X=int(input("Please enter the first number"))
Y=int(input("Please enter the second number"))

suma(X,Y)
dif(X,Y)
pro(X,Y)
div(X,Y)
rem(X,Y)
