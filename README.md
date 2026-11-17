# To-Do CLI App

A command-line to-do app written in Python. Add tasks (with an optional priority), mark them complete, and delete them. Your list is saved automatically, so it is still there the next time you open the app.

## Features
- Add tasks, with an optional priority (low, medium, high)
- Show tasks as a numbered list
- Mark tasks as complete
- Delete tasks
- Saves to a JSON file after every change
- Handles bad input without crashing

## Requirements
- Python 3 (built with [your Python version])
- No extra libraries needed

## How to run
```
git clone [your repo link]
cd [your folder name]
python todo.py
```

## Usage example
```
1. Add  2. Show  3. Complete  4. Delete  5. Exit
Choose: 1
Task title: Buy milk
Priority (low/medium/high, or press Enter to skip):

Choose: 1
Task title: Pay rent
Priority (low/medium/high, or press Enter to skip): high

Choose: 2
1 [ ] Buy milk
2 [ ] Pay rent (high)

Choose: 3
Task number: 2
Done!

Choose: 2
1 [ ] Buy milk
2 [x] Pay rent (high)

Choose: 3
Task number: abc
Please type a number.
```

## How it works
The app uses three classes:

| Class | Job |
|---|---|
| `Task` | One task: a title and a done status |
| `PriorityTask` | Extends `Task` and adds a priority |
| `TaskList` | Holds all tasks and handles add, complete, delete, save, and load |

## How saving works
Tasks are stored in `tasks.json`. Each task is turned into a dictionary with `to_dict()` and written with the `json` module. When the app starts, it loads the file and rebuilds the `Task` and `PriorityTask` objects. If the file is missing or damaged, the app starts with an empty list instead of crashing.

`tasks.json` is created automatically and is listed in `.gitignore`.

## Concepts used
- Classes and objects
- Inheritance (`PriorityTask` extends `Task` using `super()`)
- Polymorphism (`show()` and `to_dict()` behave differently for each class)
- `try/except` for input and file errors
- Reading and writing JSON

## Edge cases handled *(keep only what your app really does)*
- Unknown menu choices
- Non-numeric task numbers
- Task numbers that are 0, negative, or too large
- Empty or blank task titles
- Missing, empty, or corrupted `tasks.json`

## Project structure
```
todo-app/
├── README.md
├── .gitignore
└── todo.py
```

## What I learned
- Forgetting `self` in a method crashes the program.
- An attribute and a method cannot share the same name.
- `input()` always returns text, so numbers need `int()` inside `try/except`.
- A child class with its own `__init__` must call `super().__init__()`.

## Possible next steps
- Due dates
- Sort tasks by priority
- Move storage from JSON to a SQL databases