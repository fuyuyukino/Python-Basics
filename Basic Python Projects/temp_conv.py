#Convert Room temperature in Celcius, Fahrenheit, and Kelvin

def main():
    c, unit, unit_type = get_input()
    conv(c, unit, unit_type)

def get_input():
    while True:
        try:
            c = float(input("Give me temperature: "))
            unit_type = (input("Give me type in C, F, K: "))
            unit = input("Convert it into C, F, K: ").upper()

            if unit not in ["F", "K", "C"] or unit_type not in ["F", "K", "C"]:
                print("Only F or K or C")
                continue

            return c, unit, unit_type

        except ValueError:
            print("Invalid temperature")

def conv(c, unit, unit_type):
    if unit == "F" and unit_type == "C":
        print((c * 9/5) + 32)
    elif unit == "K" and unit_type == "C":
        print(c + 273.15)
    elif unit == "C" and unit_type == "F":
        print((c - 32) * 5/9)
    elif unit == "K" and unit_type == "F":
        print((c - 32) * 5/9 + 273.15)
    elif unit == "C" and unit_type == "K":
        print(c - 273.15)
    elif unit == "F" and unit_type == "K":
        print((c - 273.15) * 9/5 + 32)
    elif unit == unit_type:
        print(c)

if __name__ == "__main__":
    main()