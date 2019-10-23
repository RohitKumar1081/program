x = list(map(int,input("Enter the no. list : ")))
print(x)

def multiply(l):
    n=l[0]
    for a in l:
        n=n*a
    print(n)

multiply(x)