def square(num):
    return num**2

my_num = [1,2,3,4,5,6]

print(list(map(square,my_num)))

def check_even(num):
    return num%2==0

print(list(filter(check_even,my_num)))

s = lambda num:print(num**2)
s(3)

