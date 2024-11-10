
def division_calculator():
    try:
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: ")) 
         
        result = numerator / denominator
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        return
    except ValueError:
        print("Error: Please enter valid numbers.")
        return
    else:
        print("The result is:", result)
        
division_calculator()