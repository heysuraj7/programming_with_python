import math

class Temperature:
    def __init__(self, temp):
        self.temp = temp
    
    def convert_to_celsius(self):
        return (self.temp - 32) * 5/9
    
    def convert_to_fahrenheit(self):
        return (self.temp * 9/5) + 32

def main():
    while (1):
        print("\nTemperature Converter")
        print("1. Fahrenheit to Celsius")
        print("2. Celsius to Fahrenheit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            temp = float(input("Enter temperature in Fahrenheit: "))
            calc = Temperature(temp)
            celsius = calc.convert_to_celsius()
            print(f"{temp}°F = {celsius:.2f}°C")

        elif choice == '2':
            temp = float(input("Enter temperature in Celsius: "))
            calc = Temperature(temp)
            fahrenheit = calc.convert_to_fahrenheit()
            print(f"{temp}°C = {fahrenheit:.2f}°F")


if __name__ == "__main__":
    main()