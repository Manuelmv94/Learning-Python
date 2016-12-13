def gcd(a,b):
    if a==b:
        return a
    elif a>b:
        if b==0:
            return a
        a=a-b
        return gcd(a,b)
    else:
        b=b-a
        if a==0:
            return b
        return gcd(a,b)

print ("This program will calculate the greatest common divisor of two positive integers")
r='y'
while r=='y' or r=='Y':
    while True:
        try:
            x=int(input('Please enter the first positive integer number: '))
            while x<0:
                print ("Error: you should enter a positive number")
                x=int(input('Please enter the first positive integer number: '))
            break
        except ValueError:
            print ('This is not an integer number, try again')
    while True:
        try:
            y=int(input('Please enter the other positive integer number: '))
            while y<0:
                print ("Error: you should enter a positive number")
                y=int(input('Please enter the other positive integer number: '))
            break
        except ValueError:
            print ('This is not an integer number, try again')
    z=gcd(x,y)
    print ("The greatest common divisor of %s and %s is: %s" %(x,y,z))
    r=input('If you want to try some other values enter Y, if not, press any other key: ')
