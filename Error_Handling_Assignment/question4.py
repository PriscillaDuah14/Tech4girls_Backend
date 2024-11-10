
#python

items = ["apple", "banana", "cherry"]
index = int(input("Enter the index of the item you want to access: "))

try:
    print("You selected:", items[index])
except IndexError:
    print("Error: The index you entered is out of bounds. Please enter a valid index between 0 and", len(items) - 1)
