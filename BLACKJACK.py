a = int(input("Enter 1 no : "))
b = int(input("Enter 2 no : "))
c = int(input("Enter 3 no : "))
s = sum([a,b,c])

def blackjack(x,y,z):

    if (s<=21):
        print(s)
    elif s>21 and (x or y or z ==11):
        print(s-10)
    else:
        print ("BUST")

blackjack(a,b,c)