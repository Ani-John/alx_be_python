FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(degree):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    return (degree - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(degree):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    return degree/CELSIUS_TO_FAHRENHEIT_FACTOR + 32


def main():
    temp = float(input("Enter the temperature to convert: "))
    degree = input("Is this temperature in Celsius or Fahrenheit? (C/F):").strip().lower()
    try:
        if degree == 'c':
            print(f"{temp}°C is {convert_to_fahrenheit(temp)}°F")
        elif degree == 'f':
            print(f"{temp}°F is {convert_to_celsius(temp)}°C")
        else:
            print("degree is invalid")
    except ValueError:
        print("temperature is invalid")
        
if __name__ == "__main__":
    main()
