s = input("Enter the string : ")

def check(str):
    u=0
    l=0
    for c in str:
            if c.isupper():
                u+=1
            elif c.islower():
                l+=1
    print(u,l)

check(s)