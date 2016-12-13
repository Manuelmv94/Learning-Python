def inverse(x):
    x=str(x)
    x=x[::-1]
    x=int(x)
    return x

print ("This program will find the Lychrel numbers on a sequence specified by you")

numbers=[]
lychrel=[]

x0=int(input("Please enter the lower bound: "))
x1=int(input("Please enter the upper bound: "))

print ("The range of numbers analyzed goes from %s to %s" %(x0,x1))

for i in range(x1-x0+1):
    numbers.append(x0)
    x0=x0+1
p=0
nl=0
l=0
for i in numbers:
    y=inverse(i)
    if i==y:
        p=p+1
    else:
        z=i+y
        y0=inverse(z)
        for i1 in range(30):
            if z==y0:
                nl=nl+1
                break
            else:
                z=z+y0
                y0=inverse(z)
                if i1==29:
                    l=l+1
                    lychrel.append(i)

print ('The number of natural palindromes is : %s' %(p))
print ('The number of Non-Lychrel numbers encountered is: %s' %(nl))
print ('The number of Lychrel number candidates is: %s' %(l))

if l!= 0:
    print ("The Lychrel number candidates are the following:")
    print (lychrel)
