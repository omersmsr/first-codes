def myGCDfunc(a, b):
    x=1
    y=1
    mylist=[]
    myseclist=[]
    while x<=a and y<=b:
        if(a%x==0):
            mylist.append(x)
        x=x+1
        if(b%y==0):
            myseclist.append(y)
        y=y+1

    mythirdlist=[]
    for x in mylist:
        if(x in myseclist):
            mythirdlist.append(x)

    t=max(mythirdlist)
    return t              
result = myGCDfunc(33333, 111111)

print(result)