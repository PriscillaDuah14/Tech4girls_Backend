def division_calculator():
    try:
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))
        
        if denominator == 0:
            print("Error: Division by zero is not allowed.")
            return
        
        result = numerator / denominator
        print("The result is:", result)
        
    except ValueError:
        print("Error: Please enter valid integers.")


division_calculator()
