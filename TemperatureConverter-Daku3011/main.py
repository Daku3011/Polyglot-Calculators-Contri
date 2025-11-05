def main():
    # Get user's choice for conversion
    choice = input("Choose conversion (°C to °F or °F to °C) [C/F]: ").upper()

    # Celsius to Fahrenheit Conversion
    if choice == 'C':
        try:
            celsius = float(input("Enter temperature in Celsius: "))
            # Formula is (C * 9/5) + 32
            fahrenheit = (celsius * 9/5) + 32
            print(f"Temperature in Fahrenheit: {fahrenheit:.2f}")
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            return 1

    # Fahrenheit to Celsius Conversion
    elif choice == 'F':
        try:
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            # Formula is (F - 32) * 5/9
            celsius = (fahrenheit - 32) * 5/9
            print(f"Temperature in Celsius: {celsius:.2f}")
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            return 1

    else:
        print("Invalid choice!")
        return 1

    return 0

if __name__ == "__main__":
    main()