import time


def introduction():
  print("Welcome to the Text Adventure Game!")
  time.sleep(1)
  print("You find yourself in a mysterious place...")
  time.sleep(1)
  print("Your choices will determine your fate.")
  time.sleep(1)
  print("Let's begin!\n")


def scenario_one():
  print("You encounter a fork in the road.")
  time.sleep(1)
  print("Which path will you choose?")
  choice = input("Enter 'left' or 'right': ").lower()
  if choice == "left":
    print("You chose the left path.")
    time.sleep(1)
    print("You discover a hidden treasure!")

  elif choice == "right":
    print("You chose the right path.")
    time.sleep(1)
    print("A wild beast attacks you!")

  else:
    print("Invalid choice. Please enter 'left' or 'right'.")
    scenario_one()


def scenario_two():
  print("You enter a dark cave.")
  time.sleep(1)
  print("You hear a faint sound echoing.")
  time.sleep(1)
  print("What will you do?")
  choice = input("Enter 'explore' or 'leave': ").lower()
  if choice == "explore":
    print("You explore the cave and find a valuable Treasure!")

  elif choice == "leave":
    print("You decide to leave the cave.")

  else:
    print("Invalid choice. Please enter 'explore' or 'leave'.")
    scenario_two()


def play_game():
  introduction()
  scenario_one()
  scenario_two()


play_game()
