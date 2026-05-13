correct_PIN=1234
while True:
    input_pin: int=int(input("Enter_PIN"))
    if input_pin== correct_PIN:
        print("Access Granted")
    
    else:
        print("Invalid PIN")
