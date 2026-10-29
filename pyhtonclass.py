import json
import os

class TaskList:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = []
        
        # Automatically try to load tasks when the program starts
        if os.path.exists(self.filename):
            self.load()

    def add_task(self, task):
        self.tasks.append(task)
        print(f"✅ Added: '{task}'")

    def save(self):
        # Save the list of tasks to a JSON file
        with open(self.filename, "w") as file:
            json.dump(self.tasks, file)
        print("💾 Tasks saved successfully!")

    def load(self):
        # Load the list of tasks from the JSON file
        try:
            with open(self.filename, "r") as file:
                self.tasks = json.load(file)
            print("📂 Tasks loaded successfully!")
        except FileNotFoundError:
            print("⚠️ No saved file found. Starting with an empty list.")
            self.tasks = []

    def show_tasks(self):
        if not self.tasks:
            print("\n📝 Your to-do list is currently empty.")
        else:
            print("\n--- Your To-Do List ---")
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")
            print("-----------------------\n")

def main():
    my_tasks = TaskList()

    while True:
        print("\n--- MENU ---")
        print("1. Add a task")
        print("2. Show tasks")
        print("3. Save tasks")
        print("4. Load tasks")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            task = input("Enter the task: ")
            my_tasks.add_task(task)
        elif choice == '2':
            my_tasks.show_tasks()
        elif choice == '3':
            my_tasks.save()
        elif choice == '4':
            my_tasks.load()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()