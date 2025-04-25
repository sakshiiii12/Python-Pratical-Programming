#A Program to Convert from Fahreheit to Celsius

def fahrenheit_to_celsius():
    try:
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))

        celsius = (5/9) * (fahrenheit - 32)

        print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")

    except ValueError:
        print("Please enter a valid number.")

fahrenheit_to_celsius()
