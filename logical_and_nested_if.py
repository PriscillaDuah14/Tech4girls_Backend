#python

# Define boolean variables
is_student = True  # Change this to True or False
is_employed = False  # Change this to True or False

# Print messages based on conditions
if is_student and is_employed:
    print("You are a working student.")
elif is_student and not is_employed:
    print("You are a student.")
elif not is_student and is_employed:
    print("You are employed but not a student.")

# Nested if statement to check age and driver's license
age = int(input("Please enter your age: "))

if age >= 18:
    has_license = input("Do you have a driver's license? (yes/no): ").strip().lower()
    if has_license == "yes":
        print("You are allowed to drive.")
    else:
        print("You need a driver's license to drive.")
else:
    print("You are not old enough to drive.")
