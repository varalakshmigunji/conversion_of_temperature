def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    print("Temperature Conversion Program")
    print("==============================")
    temperature = float(input("Enter the temperature value: "))
    unit = input("Enter the unit of measurement (C for Celsius, F for Fahrenheit): ")

    if unit.upper() == 'C':
        converted_temperature = celsius_to_fahrenheit(temperature)
        print(f"{temperature}°C is equal to {converted_temperature}°F.")
    elif unit.upper() == 'F':
        converted_temperature = fahrenheit_to_celsius(temperature)
        print(f"{temperature}°F is equal to {converted_temperature}°C.")
    else:
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

if __name__ == "__main__":
    main()