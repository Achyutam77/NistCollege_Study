def get_subjects_and_marks(num_subjects):
    subjects = {}
    for i in range(num_subjects):
        subject_name = input(f"Enter name of subject #{i+1}: ")
        while True:
            try:
                marks = float(input(f"Enter marks for {subject_name} (out of 100): "))
                if 0 <= marks <= 100:
                    break
                else:
                    print("Marks should be between 0 and 100. Try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        subjects[subject_name] = marks
    return subjects

def calculate_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    else:
        return "Fail"

def main():
    print("Welcome to the Student Report Card Generator!")
    student_name = input("Enter the student's name: ")
    while True:
        try:
            num_subjects = int(input("How many subjects does the student have? "))
            if num_subjects > 0:
                break
            else:
                print("Number of subjects must be positive.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

    subjects = get_subjects_and_marks(num_subjects)
    total_marks = sum(subjects.values())
    average_marks = total_marks / num_subjects
    grade = calculate_grade(average_marks)

    print(f"\n----- Report Card for {student_name} -----")
    print("Subjects:")
    for subject, marks in subjects.items():
        print(f"{subject}: {marks}")
    print(f"\nTotal Marks: {total_marks}")
    print(f"Average Marks: {average_marks:.2f}")
    print(f"Grade: {grade}")
    print("-------------------------------")

if __name__ == "__main__":
    main()