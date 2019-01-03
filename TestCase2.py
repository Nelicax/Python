# Defining Array Lists First that comply with the High-School system.

A = [19, 20]
B = [16, 17, 18]
C = [13, 14, 15]
D = [10, 11, 12]
E = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Greeting the app user.

print("Welcome to Grading Assistant 1.0")

# Defining infinite loop so the teacher can continue consulting grades.

while True:

    # Sharing instructions to receive from the user the quantity of grade to evaluate.

    try: # try-catch exception to make sure the user is entering a number.
        Grade = (input("Please enter the student's score in numbers: "))
        Grade = (int(Grade))  # Casting the variable into a integer type.
    except:
        print("Please type the students score in numbers")
    else:
        if Grade >=1 and Grade <= 20: # To make sure the user is entering a score between 1 and 20 only.
            if Grade in A:
                print("The letter to grade the student should be A")
            if Grade in B:
                print("The letter to grade the student should be B")
            if Grade in C:
                print("The letter to grade the student should be C")
            if Grade in D:
                print("The letter to grade the student should be D")
            if Grade in E:
                print("The letter to grade the student should be E")
        else:
                print("The student's score cannot be either smaller than 0 or higher than 20. Please Try again")






