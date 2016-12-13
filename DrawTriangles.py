#Manuel Madrigal Valenzuela

def triangles(a):
    if a < 2:
        print ('You need a number equal or bigger than two to see the triangle')
    else:
        for i in range(1,a+1):
            print("T"*i)
            if i==a:
                n=i-1
                while n > 0:
                    print("T"*n)
                    n=n-1

print('This program will print a triangle with a provided size for the middle line')
r='y'

while r=='y' or r=="Y":
    while True:
        try:
            x=int(input('Please enter an integer number for the size of the triangle: '))
            break
        except ValueError:
            print('This is not an integer number, Please try again')

    triangles(x)
    r=input("Please enter Y if you want to try another size, if not, enter any other key: ")
