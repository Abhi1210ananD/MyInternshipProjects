def celsius_to_fahrenheit(celsius):
  return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
  return (fahrenheit - 32) * 5 / 9


def meters_to_feet(meters):
  return meters * 3.28084


def feet_to_meters(feet):
  return feet / 3.28084


def kilograms_to_pounds(kilograms):
  return kilograms * 2.20462


def pounds_to_kilograms(pounds):
  return pounds / 2.20462


def unit_converter():
  print("Welcome to the Unit Converter!")

  print("Select the conversion type:")
  print("1. Temperature Converter (Celsius to Fahrenheit )")
  print("2. Length Converter (Meters to Feet )")
  print("3. Weight Converter (Kilograms to Pounds )")

  conversion_type = input("Enter the option (1, 2, or 3): ")

  try:
    value = float(input("Enter the value to convert: "))
  except ValueError:
    print("Invalid input. Please enter a numeric value.")
    return

  if conversion_type == '1':
    converted_value = celsius_to_fahrenheit(value)
    print(f"{value} Celsius is equal to {converted_value:.2f} Fahrenheit.")
  elif conversion_type == '2':
    converted_value = meters_to_feet(value)
    print(f"{value} Meters is equal to {converted_value:.2f} Feet.")
  elif conversion_type == '3':
    converted_value = kilograms_to_pounds(value)
    print(f"{value} Kilograms is equal to {converted_value:.2f} Pounds.")
  else:
    print("Invalid option. Please enter 1, 2, or 3.")


if __name__ == "__main__":
  unit_converter()
