while(True):
    try:
        number_1 = int(input("Enter the first number: "))
        if number_1 == 'q':
            raise Exception
        number_1 = int(number_1)

        operator = input("Enter the operator (+, -, *, or /): ")
        if operator == 'q':
            raise Exception
        
        number_2 = input("Enter the second number: ")
        if number_2 == 'q':
            raise Exception
        number_2 = int(number_2)
        if (operator == "/" and number_2 == 0):
            raise ZeroDivisionError
        
    except ValueError:
        print("One of the values you entered as a number is not valid.")
    except ZeroDivisionError:
        print("Can't divide by zero.")
    except Exception:
        print("You have terminated the program.")
        break
    else:
        if operator == "+":
            result = number_1+number_2
        elif operator == "-":
            result = number_1-number_2
        elif operator == "*":
            result = number_1*number_2
        elif operator == "/":
            result = number_1/number_2
        print(f"The answer of {number_1} {operator} {number_2} is equal to: {result}.")
    finally:
        print("Attempt complete.")