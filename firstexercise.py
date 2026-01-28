import random
mylist=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

while True:
    x=""
    t=""
    myseclist=[]
    mythirdlist=[]
    print("enter length of words")
    lengthof_words=int(input())
    for _ in range(lengthof_words):
        t=random.choice(mylist)
        myseclist.append(t)
    for _ in range(lengthof_words):
        x=input()
        mythirdlist.append(x)

    print(myseclist)
    print("******")
    print(mythirdlist)
    rights=lengthof_words
    for x in range(lengthof_words):
        if(myseclist[x]==mythirdlist[x]):
            rights+=0
        else:
            rights-=1
    if(rights==0):
        raise ValueError("your rights are over")
    elif(rights >0):
        print(f'your {rights} rights left')
        
        
    

    
