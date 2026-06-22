#Trial to Login
user = {
    "username" : "FUYU",
    "password" : "{|}A0lp(ha){|}"
}

#Set number attempts to 3
attempts_number = 5
attempts = 0

#Input username & password
def main():
    global attempts
    global attempts_number
    while attempts < attempts_number:
        enter_username = input("Username: ")
        enter_password = input("Password: ")
        
        #Comparing value
        if (enter_username == user["username"] 
            and enter_password == user["password"]):
            print("Correct")
            return
        
        attempts += 1
        print("Invalid Number")
    
    print("Account Locked.")

main()