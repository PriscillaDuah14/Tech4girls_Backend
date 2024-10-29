#if-else
#python

age = int(input("please enter your age:"))
#check the age and print the corresponding message

if age < 18 :
    print("you are a minor")
elif 18 <= age <= 64:
    print("you are an adult")
else:
    print("you are senior")

