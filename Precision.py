def fact(n):
    if n==0 or n==1:
        return n
    else:
        return n*fact(n-1)

def calculate_e(precision):
    i=1
    e=1
    g=0
    ng=1/fact(i)
    e=e+ng
    i=i+1
    while g != ng:
        g=ng
        ng=1/fact(i)
        e=e+ng
        i=i+1
    return round(e,precision)

y=calculate_e(5)
print (y)
