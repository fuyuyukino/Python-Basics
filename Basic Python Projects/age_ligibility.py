#Checking eligibility of age to vote

while True:
    try:
        i = int(input("What's your age? "))
    except ValueError:
        print("Invalud input")
    else:
        break

def vote():
    if i >= 18:
        print('You can vote now')
    else:
        print("You're still underage")

vote()