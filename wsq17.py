def movies(a):
    f=open(a,'r')
    Dict={}
    for i in f:
        c0=i.find(',')
        c2=i.find(',',(c0+1))
        mov=i[(c0+2):(c2)]
        if Dict.get(mov)==None:
            Dict[mov]=[i[0:c0]]
        else:
            Dict[mov].append(i[0:c0])
        while c2!=(-1):
            c1=c2
            c2=i.find(',',(c1+1))
            mov=i[(c1+2):c2]
            if Dict.get(mov)==None:
                Dict[mov]=[i[0:c0]]
            else:
                Dict[mov].append(i[0:c0])
    return Dict

def check_movies(a,b):
    Dict0=movies('movies.txt')
    x=Dict0.get(a)
    y=Dict0.get(b)
    Dict1={}
    lista=[]
    listb=[]
    listc=[]
    for i in x:
        if Dict1.get(i)==None:
            Dict1[i]=[a]
        else:
            Dict1[i].append(a)
    for i in y:
        if Dict1.get(i)==None:
            Dict1[i]=[b]
        else:
            Dict1[i].append(b)

    for i in Dict1:
        lista.append(i)
        if len(Dict1.get(i))==2:
            listb.append(i)
        elif len(Dict1.get(i))==1:
            listc.append(i)
    print()
    print('All the actors in those movies are: ')
    print(lista)
    print('The common actors in the 2 movies are: ',listb)
    print('The actors who are in either of the movies but not both are: ')
    print(listc)

def check_coactors(act):
    Dict0=movies('movies.txt')
    lista=[]
    listb=[]
    listc=[]
    Dict1={}
    for i in Dict0:
        for j in (Dict0.get(i)):
            if j==act:
                lista.append(i)
    for i in lista:
        for j in (Dict0.get(i)):
            if j != act:
                listb.append(j)
    for i in listb:
        if Dict1.get(i)==None:
            Dict1[i]=[1]
        else:
            Dict1[i].append(1)
    for i in Dict1:
        listc.append(i)
    print()
    print('All the actors with whom he/she has acted are: ')
    print(listc)

#Here is where the user-interactive program starts
print('Welcome to our movies database')
r='y'
while r=='y':
    print()
    print('You have 2 options:')
    print('a) Enter the name of two movies to get the actors')
    print('b) Enter the name of an actor to get the co-actors ')
    x=input('Select an option(a/b): ')
    while (x!='a' and x!='b'):
        print('Invalid command')
        x=input('Select an option(a/b): ')
    if x=='a':
        r1=input('Please enter the first movie: ')
        r2=input('Please enter the second movie: ')
        check_movies(r1,r2)
    else:
        r1=input('Please enter the name of the actor: ')
        check_coactors(r1)
    print()
    r=input('Enter (y) if you want to go back to the main menu or any other character if you want to exit: ')
