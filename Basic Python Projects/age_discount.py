2#Define the discount for Senior age using Boolean
Age = int(input("What's your age? "))
is_member = True

def Discount(Age):
    if Age >= 60:
        if is_member:
            print("You have 50% discount")
        else:
            print("You have 20% discount")
    else:
        print("You're not eligible for senior discount")

Discount(Age)