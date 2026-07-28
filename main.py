import addition
import division
import square_root
import subtraction
import multiplication
import square
import square_root
import percentage
def main():
    print("------------ Calculator --------- ")
    
    try:
        select_option = int(input("Select an option:\n0. Exit\n1. Addition\n2. Subtraction\n3. Division\n4. Multiplication\n5. Square\n6. Square Root\n7. Percentage\n"))
    except ValueError:
        print("Invalid input. Please enter valid integers.")
        return
    if select_option == 0:
        print("Exiting the calculator.")
        return    
    elif select_option in [5, 6]:
        try:
            num = int(input("Enter a number: "))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            return
    elif select_option in [1, 2, 3, 4, 7]:
        try:
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter valid integers.")
            return
    else:
        print("Invalid option selected.")
        return
    if select_option == 0:
        print("Exiting the calculator.")
    elif select_option == 1:
        result = addition.add(num1,num2)
        print("The sum is:",result)
    elif select_option == 2:
        result = subtraction.sub(num1,num2)
        print("The difference is:",result)
    elif select_option == 3:
        result = division.div(num1,num2)
        print("The quotient is:",result)
    elif select_option == 4:
        result = multiplication.multiply(num1,num2)
        print("The product is:",result)
    elif select_option == 5:
        result = square.square(num)
        print("The square is:",result)
    elif select_option == 6:
        result = square_root.square_root(num)
        print("The square root is:",result)
    elif select_option == 7:
        result = percentage.percentage(num1,num2)
        print("The percentage is:",result)
    else:
        print("Invalid option selected.")

if __name__ == "__main__":
    main()