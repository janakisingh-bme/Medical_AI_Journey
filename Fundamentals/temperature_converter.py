# Temperature Converter

temperature = float(input("Enter temperature: "))

choice = input("Convert to (C)elsius or (F)ahrenheit? ")

if choice.upper() == "F":
    fahrenheit = (temperature * 9 / 5) + 32
    print("Temperature in Fahrenheit:", round(fahrenheit, 2))

elif choice.upper() == "C":
    celsius = (temperature - 32) * 5 / 9
    print("Temperature in Celsius:", round(celsius, 2))

else:
    print("Invalid choice.")