data = {"name": "Prissy", "age": 25, "country": "Accra"}
key = input("Enter the key you want to look up: ")

try:
    print("Value:", data[key])
except KeyError:
    print("Error: The key you entered does not exist in the dictionary.")
