name=input("Enter your name: ")
sub=int(input("Enter the number of subjects: "))

def total_marks(math=None, science=None, english=None, nepali=None, social=None):
    return math + science + english+ nepali + social
def average_marks(total_mark(), sub):
    return total_mark() / sub

for i in range(sub):
    name = input("Enter the name of the subject: ")
    marks = int(input(f"Enter the marks obtained in {name}: "))
    if marks >= 90:
        print("Grade=A+")
    elif marks >= 80:
        print("Grade=A")        
    elif marks >= 70:
        print("Grade=B")
    elif marks >= 60:
        print("Grade=C")
    else:
        print("Failed")

print(f"-----Report Card of {name}-----")}")
    printf("Subject:")
    printf("Math")
    print(f"Total Marks: {total_marks()}")
    print(f"Average Marks: {average_marks(total_marks(), sub)}")


