import random
import string


def generate_password(length=12):
  characters = string.ascii_uppercase + string.ascii_lowercase + string.digits + '!@#$%^&*()_-+='
  password = ''.join(random.choice(characters) for _ in range(length))
  return password


def main():
  print("Welcome to the Password Generator!")

  try:
    num_passwords = int(input("Enter the number of passwords to generate: "))
    password_length = int(
        input("Enter the desired length for each password: "))
  except ValueError:
    print("Invalid input. Please enter a valid number.")
    return

  print("\nGenerated Passwords:")
  for _ in range(num_passwords):
    password = generate_password(password_length)
    print(password)

  print("\nPassword generation complete.")


if __name__ == "__main__":
  main()
