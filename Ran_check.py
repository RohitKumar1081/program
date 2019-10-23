x = int(input("Enter the no : "))
y = int(input("Enter the lower range : "))
z = int(input("Enter the higher range : "))

def ran_check(num,low,high):
    print(num in range(low, high))

ran_check(x,y,z)