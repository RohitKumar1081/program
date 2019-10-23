name = " This is the Global String "

def greet():
    name = "Sammy"

    def hello():
        name = "I'm Local"
        print("Hello "+name)
    hello()

greet()


x = 50
def func(x) :
    #global x
    print(f"The Global value is {x}")
    x= 'New Value'
    print(f"The local value is {x}")
    return x

#func()
x = func(x)
print(x)