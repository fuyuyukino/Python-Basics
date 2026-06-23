#Choose random temperature and make conditional
import random

Temperature = random.randrange(-30, 100, 10)
print("The temperature today is " + str(Temperature))

def temp(Temperature):
    if Temperature >= 40:
        print("It's hot today!!")
    elif Temperature >= 20:
        print("Warm temperature, I like it")
    elif Temperature >= 0:
        print("Today, it's a bit cold")
    else:
        print("I'm freezing")

temp(Temperature)