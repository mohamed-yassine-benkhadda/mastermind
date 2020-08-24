from getpass import getpass

def settings():
    l=int(input("the code contains : "))
    m=int(input("max attempts : "))
    return l,m


def code(l):
    print("rules : 1. the code contains",l,"characters      2.Don't repeat characters")
    x=getpass("enter the code :")
    if len(x)!=l:
        return code(l)
    for i in range(l):
        for j in range(l):
            if x[i]==x[j] and i!=j:
                return code(l)
    return x



def answer(l):
    x=input("enter the code :")
    if len(x)!=l:
        return answer(l)
    for i in range(l):
        for j in range(l):
            if x[i]==x[j] and i!=j:
                return answer(l)
    return x


def exact_place(a,c,l):
    q=0
    for i in range(l):
        if a[i]==c[i]:
            q+=1
    return q


def change_place(a,c,l):
    q=0
    for i in range(l):
        for j in range(l):
            if a[i]==c[j] and i!=j:
                q+=1
    return q

def menu():
    q=int(input("1.play again 2.exit"))
    if q==1:
        return game()

def game():
    l,m = settings()
    c=code(l)
    a=c[:l-1]+c[0]
    ex=exact_place(a,c,l)
    i=0
    print("guess the secret code using the hints")
    while ex!=l and i<m:
        print(m-i," attempts left")
        a=answer(l)
        ex=exact_place(a,c,l)
        ch=change_place(a,c,l)
        print("correct : ",ex)
        print("change : ",ch)
        i+=1
    if i<m:
        print("congrats,you win ",i," attempts")
    else:
        print("hard luck")
    return menu()
    
game()



