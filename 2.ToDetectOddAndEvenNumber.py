#A Program to Detect Odd and Even Numbers:

def DetectNum(numbers):
    Even_Numbers = []
    Odd_Numbers = []

    for num in numbers:
        if (num%2==0):
            Even_Numbers.append(num)
        else:
            Odd_Numbers.append(num)

    return Even_Numbers, Odd_Numbers

def main():
    print("Odd and Even Number Classifier")
    input_num = input("Enter a list of numbers separated by spaces: ")

    try:
        numbers = list(map(int, input_num.split()))
    except ValueError:
        print("Invalid input. Please enter only numbers.")
        return

    Even_Numbers, Odd_Numbers = DetectNum(numbers)

    print("\nResults:")
    print(f"Even Numbers: {Even_Numbers}")
    print(f"Odd Numbers: {Odd_Numbers}")

if __name__ == "__main__":
    main()
