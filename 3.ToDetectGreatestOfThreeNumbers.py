#A Program to Detect the Greatest of Three Numbers:

def find_greatest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


def main():
    print("Greatest of Three Numbers")

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        num3 = float(input("Enter the third number: "))
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        return

    greatest = find_greatest(num1, num2, num3)
    print(f"\nThe greatest number is: {greatest}")


if __name__ == "__main__":
    main()
