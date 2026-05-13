username=("admin")
password=1234
un= str(input("Enter Username"))
pw= int(input("Enter password"))
if username==un:
    if pw==password:
        print("Log in Successfull")
    else:
        print("Invalid User name or Password")
