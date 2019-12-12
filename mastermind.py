#try to test that program in a performer compiler
#the game requires two players the firstgonna set a code and the other must find it using games hints
from getpass import getpass
r=1
w=4
p=1
n=10
while p==1:
    if r==2:
        w=int(input("length of code:"))
        n=int(input("max attempts:"))
        r=1
    if r==3:
        p=0
    while r==1:
        x=getpass("enter code")
        while len(x)!=w:
            x=getpass("enter code")
        for i in range(w):
            for q in range(w):
                while x[i]==x[q] and i!=q:
                    print("do not repeat characters")
                    x=getpass("enter code")
        y=input("to start press any button")
        l=0
        while x!=y and l<n+1:
            c=0
            m=0
            y=input()
            if len(y)!=w:
                print("the code contain",w,"characters")
            else:
                l=l+1
                for i in range(w):
                    if x[i]==y[i]:
                        c=c+1
                    for q in range(w):
                        if x[i]==y[q] and i!=q:
                            m=m+1
                print("correct:",c,"change:",m)
        if x==y:
            print("congratulations,attempts:",l)
        if x!=y:
            print("hard luck next time")
            print("the code is :",x)
        r=int(input("1.play again    2.settings     3.leave"))
