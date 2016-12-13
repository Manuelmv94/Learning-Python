fr=open("93cars.dat.txt","r")
mpgc=0
mpgh=0
mprice=0
cars=0
f=1
for line in fr:
    if f%2==1:
        mpgc=mpgc+float(line[52:54])
        mpgh=mpgh+float(line[55:57])
        mprice=mprice+float(line[42:46])
        cars=cars+1
    f=f+1
x=round(mpgc/cars,6)
y=round(mpgh/cars,6)
z=round(mprice/cars,6)

print("The average gas mileage in city(City MPG) is: ", x)
print("The average gas mileage on highway (Highway MPG) is: ",y)
print('The average midrange price of the vehicles in the set is: ',z)
