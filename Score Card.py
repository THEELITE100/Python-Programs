subject1 = int(input("Enter marks of the first subject out of 100: "))
subject2 = int(input("Enter marks of the second subject out of 100: "))
subject3 = int(input("Enter marks of the third subject out of 100: "))
subject4 = int(input("Enter marks of the fourth subject out of 100: "))
subject5 = int(input("Enter marks of the fifth subject out of 100: "))
total = subject1+subject2+subject3+subject4+subject5
print("Total Marks:",total)
percentage = (total/500)*100
print("Percentage:",percentage)
if(percentage>=85):
    print("Grade: A")
elif(percentage>=70 and percentage<85):
    print("Grade: B")
elif(percentage>=60 and percentage<70):
    print("Grade: C")
elif(percentage>=50 and percentage<60):
    print("Grade: D")
elif(percentage>=40 and percentage<50):
    print("Grade: E")
else:
    print("Grade: F")