#A Program to Detect Positive and Negative Numbers:

def DetectNum(numbers):
    positives = []
    negatives = []
    zeros = []

    for num in numbers:
        if num > 0:
            positives.append(num)
        elif num < 0:
            negatives.append(num)
        else:
            zeros.append(num)

    return positives, negatives, zeros


def main():
    print("Positive and Negative Number Classifier")
    input_str = input("Enter a list of numbers separated by spaces: ")

    try:
        numbers = list(map(float, input_str.split()))
    except ValueError:
        print("Invalid input. Please enter only numbers.")
        return

    positives, negatives, zeros = DetectNum(numbers)

    print("\nResults:")
    print(f"Positive numbers: {positives}")
    print(f"Negative numbers: {negatives}")
    print(f"Zeros: {zeros}")


if __name__ == "__main__":
    main()
