#Manuel Madrigal Valenzuela

def find_threes (a):
    sm=0
    for i in a:
        y=i%3
        if y==0:
            sm=sm+i
    return sm

print('This program will calculate the sum of all numbers in a list that are even divisible by 3')

r='y'
while r== 'y' or r== 'Y':

    z=[]
    while True:
        try:
            p=int(input('How many elements are going to be on your list? '))
            if p<1:
                p=int(input('There has to be at least 1 element. Please try again: '))
            break
        except ValueError:
            print("This is not an integer number. Please try again")

    for i in range(p):
        while True:
            try:
                e=int(input('Enter the element number %s of your list: ' %(i+1)))
                break
            except ValueError:
                print('This is not an integer number. Please try again')
        z.append(e)

    x=find_threes(z)
    print('The sum of the numbers on the list that are even divisible by 3 is: %s' %x)

    r=input('Enter Y if you want to try another list, if not, type any other key: ')
