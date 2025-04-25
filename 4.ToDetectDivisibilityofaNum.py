#A Program to Check for Divisibility of a Number

def check_divisibility():
    try:
        num = int(input("Enter the number to be divided: "))
        divisor = int(input("Enter the divisor: "))
        
        if divisor == 0:
            print("Divisor cannot be zero.")
            return

        if num % divisor == 0:
            print(f"{num} is divisible by {divisor}.")
        else:
            print(f"{num} is NOT divisible by {divisor}.")

    except ValueError:
        print("Please enter valid integers.")

check_divisibility()
