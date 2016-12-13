print ("This Program will calculate the sum of integers in the range you provide")
print("Please enter the lower bound")
x=int(input())
print("Please enter the upper bound")
y=int(input())
l=x
u=y
if y < x:
	l=y
	u=x
	print ("Oops! Seems like you entered the bounds in the wrong order, but we changed them for you")
s=0
z=u-l+1
i=0
while i != z:
	s=s+l
	l=l+1
	i=i+1
print ("The sum of integers in the range you provided is:",s)
