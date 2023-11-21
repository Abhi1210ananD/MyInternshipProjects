class Task:

  def __init__(self, description, due_date, priority):
    self.description = description
    self.due_date = due_date
    self.priority = priority
    self.completed = False

  def complete(self):
    self.completed = True

  def __str__(self):
    return f"{self.description} ({self.due_date}, {self.priority}) - {'Completed' if self.completed else 'Incomplete'}"


class TaskList:

  def __init__(self):
    self.tasks = []

  def add_task(self, description, due_date, priority):
    self.tasks.append(Task(description, due_date, priority))

  def display_tasks(self):
    for task in self.tasks:
      print(task)

  def complete_task(self, description):
    for task in self.tasks:
      if task.description == description:
        task.complete()
        break

  def update_task(self, description, new_description, new_due_date,
                  new_priority):
    for task in self.tasks:
      if task.description == description:
        task.description = new_description
        task.due_date = new_due_date
        task.priority = new_priority
        break

  def remove_task(self, description):
    self.tasks = [
        task for task in self.tasks if task.description != description
    ]


task_list = TaskList()

while True:
  print("\n1. Add Task")
  print("2. Display Tasks")
  print("3. Complete Task")
  print("4. Update Task")
  print("5. Remove Task")
  print("6. Exit")

  option = int(input("Enter the option number: "))

  if option == 1:
    description = input("Enter task description: ")
    due_date = input("Enter due date (DD/MM/YYYY): ")
    priority = input("Enter priority (Low, Medium, High): ")
    task_list.add_task(description, due_date, priority)

  elif option == 2:
    task_list.display_tasks()

  elif option == 3:
    description = input("Enter task description: ")
    task_list.complete_task(description)

  elif option == 4:
    description = input("Enter current task description: ")
    new_description = input("Enter new task description: ")
    new_due_date = input("Enter new due date (DD/MM/YYYY): ")
    new_priority = input("Enter new priority (Low, Medium, High): ")
    task_list.update_task(description, new_description, new_due_date,
                          new_priority)

  elif option == 5:
    description = input("Enter task description: ")
    task_list.remove_task(description)

  elif option == 6:
    break

  else:
    print("Invalid option. Please try again.")