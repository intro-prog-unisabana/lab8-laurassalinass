import sys
import os


def read_tasks(file_path):
    if not os.path.exists(file_path):
        print(f"File {file_path} not found! Returning an empty to-do list.")
        return []

    with open(file_path, "r") as file:
        return [line.strip() for line in file if line.strip()]


def write_tasks(file_path, tasks):
    with open(file_path, "w") as file:
        for task in tasks:
            file.write(task + "\n")


def print_tasks(tasks):
    print("Tasks:")
    for task in tasks:
        print(task)


def main():
    args = sys.argv[1:]

    if len(args) == 0:
        print("Insufficient arguments provided!")
        return

    if args[0] in ["help", "--help", "-h"]:
        print("Usage: python main.py <file_path> <command> [arguments]...")
        return

    if len(args) == 1:
        return

    file_path = args[0]
    commands = args[1:]

    tasks = read_tasks(file_path)
    changed = False

    i = 0
    while i < len(commands):
        command = commands[i]

        if command == "view":
            print_tasks(tasks)
            i += 1

        elif command == "add":
            if i + 1 >= len(commands):
                print('Task description required for "add".')
                return

            task = commands[i + 1]
            tasks.append(task)
            changed = True
            print(f'Task "{task}" added.')
            i += 2

        elif command == "remove":
            if i + 1 >= len(commands):
                print('Task description required for "remove".')
                return

            task = commands[i + 1]

            if task in tasks:
                tasks.remove(task)
                changed = True
                print(f'Task "{task}" removed.')
            else:
                print(f'Task "{task}" not found.')

            i += 2

        else:
            print("Command not found!")
            return

    if changed:
        write_tasks(file_path, tasks)


if __name__ == "__main__":
    main()