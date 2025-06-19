age=int(input("Enter your age: "))
gender=input("Enter your gender: ")
if age >=18:
    if gender == "male":
        print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")  