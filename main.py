import sys
import os

USAGE = """Usage:
python3 todo.py view <filename>
python3 todo.py add <filename> <task>
python3 todo.py remove <filename> <task>
"""

def read_tasks(filename):
    if not os.path.exists(filename):
        return []

    with open(filename, "r") as file:
        return [line.strip() for line in file if line.strip()]

def write_tasks(filename, tasks):
    with open(filename, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def main():
    args = sys.argv[1:]

    if len(args) == 0:
        return

    command = args[0]

    if command in ["help", "--help", "-h"]:
        print(USAGE)
        return

    if len(args) < 2:
        print(USAGE)
        return

    filename = args[1]

    if command == "view":
        tasks = read_tasks(filename)
        for task in tasks:
            print(task)
        return

    elif command == "add":
        if len(args) < 3:
            print("Missing task")
            return

        task = " ".join(args[2:])
        tasks = read_tasks(filename)
        tasks.append(task)
        write_tasks(filename, tasks)
        return

    elif command == "remove":
        if len(args) < 3:
            print("Missing task")
            return

        task = " ".join(args[2:])
        tasks = read_tasks(filename)

        if task in tasks:
            tasks.remove(task)
            write_tasks(filename, tasks)
        else:
            print("Task not found")
        return

    else:
        print("Invalid command")
        return


if __name__ == "__main__":
    main()