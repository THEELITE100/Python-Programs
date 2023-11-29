#Travel Agency
travelling = input("Yes or No: ")
while travelling == ("Yes"):
    num = int(input("Number Of People Travelling: "))
    for num in range(1,num+1):
        name = input("Name: ")
        age = input("Age: ")
        sex = input("Male or Female: ")
        print(name)
        print(age)
        print(sex)
    travelling = input("Oops! Forget Someone: ")
    break
print("Thank You For Travelling With Us :)")