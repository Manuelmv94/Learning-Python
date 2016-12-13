print ("This program will generate a random number from 0 to 100. Try to guess it!")
import random
x= random.randrange(0,100)
print ("Please enter a guess of the number")
y=int(input())
while y != x:
	if y < x :
		print ("Sorry, too low. Keep trying")
		y=int(input())
	if y > x:
		print ("Sorry,too high. Keep trying")
		y=int(input())
print ("Congratulations! You have found the number")
