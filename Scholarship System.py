# Input Data
name = input("Enter Your Name: ")
roll_no = int(input("Enter Your Roll_no: "))
Tot_Sub = int(input("Enter the Total number of Subjects: "))
marks = input("Enter the Marks of Each subject: ").split()

if len(marks) == Tot_Sub:

    # Convert to integers
    marks = list(map(int, marks))

    # Check each subject mark
    is_failed = False
    for mark in marks:
        if mark < 35:
            is_failed = True
            break

    Total_marks = sum(marks)
    Average = Total_marks / Tot_Sub

    print("\n----- Student Report -----")
    print(f"Name: {name}")
    print(f"Roll No: {roll_no}")
    print(f"Total Marks: {Total_marks}")
    print(f"Average: {Average}")

    # Result & Grade
    if is_failed:
        print("Result: Failed")
    else:
        if Average >= 90:
            print("Grade: A")
        elif Average >= 80:
            print("Grade: B")
        elif Average >= 70:
            print("Grade: C")
        elif Average >= 50:
            print("Grade: D")
        else:
            print("Grade: E")

    # Scholarship
    if not is_failed and Average >= 80:
        print("Scholarship: Eligible")
    else:
        print("Scholarship: Not Eligible")

else:
    print(f"Enter only the {Tot_Sub} subject marks. Try Again")
