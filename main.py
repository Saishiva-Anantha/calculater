import addition
import subtraction

def main():
    print("------------ Calculator --------- ")
    
    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please enter valid integers.")
        return
    
    select_option = int(input("Select an option:\n0. Exit\n1. Addition\n2. Subtraction\n"))
    
    if select_option == 0:
        print("exit")
        return
    elif select_option == 1:
        result = addition.add(num1,num2)
        print("The sum is:",result)
    elif select_option == 2:
        result = subtraction.sub(num1,num2)
        print("The difference is:",result)
    else:
        print("Invalid option selected.")

if __name__ == "__main__":
    main()