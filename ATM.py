#nested loop
print("Welcome To Iron Bank Of Voos ATM")
restart = ("Y")
chances = 3
balance = 257.752
while chances >= 0:
    pin = int(input("Please Enter Your 4 Digit Pin:"))
    if pin == (1234):
        print("You entered your pin Correctly\n")
        while restart not in ("n","NO","no","N"):
            print("Please Press 1 For Your Balance\n")
            print("Please Press 2 To Make Withdrawl\n")
            print("Please Press 3 To Pay In\n")
            print("Please Press 4 To Return Card\n")
            option = int(input('What Would You Like To Choose?'))
            if option == 1:
                print("Your Balance is $",balance,"\n")
                restart = input("Would You Like To Go Back?")
                if restart in ("n","NO","no","N"):
                    print("Thank You")
                    break
            elif option == 2:
                option2 = ("y")
                Withdrawl = float(input("How much would oyu like to Withdrawl\n$10/$20/$40/$60/$80/$100"))
                if Withdrawl in [10,20,40,60,80,100]:
                    balance = balance - Withdrawl
                    print("\nYour Balance is now $",balance)
                    restart = input("Would You Like To Go Back?")
                    if restart in ("n","NO","no","N"):
                        print("Thank You")
                        break
                elif Withdrawl != [10,20,40,60,80,100]:
                    print("Invalid Amount, Please Re-try\n")
                    restart = ("y")
                elif Withdrawl == 1:
                    Withdrawl = float(input("Please Enter Desired Amount"))
            elif option == 3:
                Pay_in = float(input("How Much Would You Like To Pay In?"))
                balance = balance + Pay_in
                print("\nYour Balance is now $",balance)
                restart = input("Would You Like To Go Back?")
                if restart in ("n","NO","no","N"):
                    print("Thank You")
                    break
            elif option == 4:
                print("Please Wait Until Your Card Is Returned...\n")
                print("Thank You For Your Service")
                break
            else:
                print("Please Enter A Correct Number.")
                restart = ("y")
    elif pin !=("1234"):
        print("Incorrect Password")
        chances = chances - 1
        if chances == 0:
            print("\nNo More Tries")
            break