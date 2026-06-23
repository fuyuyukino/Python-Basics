'''
Conditional using if, elif, and else command
in Python. Conditionals can use operations like
== (Equal), != (Not Equal), and another operations
'''

#Define the condition of x and y
x = float(input("What's X? "))
y = float(input("What's Y? "))  
  
def condition(x,y):
    if x == y:
        print("X is equal to Y")
    elif x > y:
        print("X is larger than Y")
    else:
        print("X is smaller than Y")

condition(x,y)



#Define the condition by !=
x = float(input("What's X? "))
y = float(input("What's Y? "))  

def condition(x,y):
    if x != y:
        print("x is not equal to y")
    else:
        print("x is equal to y")

condition(x,y)



#Define the condition by ==
x = float(input("What's X? "))
y = float(input("What's Y? "))  

def condition(x,y):
    if x == y:
        print("x is equal to y")
    else:
        print("x is not equal to y")

condition(x,y)