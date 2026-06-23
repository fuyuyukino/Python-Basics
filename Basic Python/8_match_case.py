#Matching expression
name = input("What's your name? ")

match name:
    case 'Amelia' | 'Griffin' | 'Sony' :
        print("AMERICA!!!")
    case 'Kyezetch' | 'Natasha' | 'Karolin':
        print("Babushki")
    case _:
        print("Go back to your nation, buddy!")