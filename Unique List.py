x = list(input("Enter the list : "))
#print(x)

def unique_list(l):
    n = []
    for a in l:
        if a not in n:
            n.append(a)
    print(n)

unique_list(x)