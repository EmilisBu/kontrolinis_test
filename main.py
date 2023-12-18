import time
# Wanted to make another check for tasks to print messages like:
# This date passed, so task can't be created, but didn't have time for that
import datetime

tasks = []


def add_task():
    name = input("Enter task name: ")
    end_date = input("Enter end date (YYYY-MM-DD): ")
    tasks.append({"name": name, "end_date": end_date})
    save_tasks()
    print("Task added")


def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(f"{task['name']},{task['end_date']}\n")


def display_tasks():
    id = 1
    if not tasks:
        print("No tasks added yet.")
    else:
        print("Task List:")
        for task in tasks:
            print(f"{id}. {task['name']} - Due: {task['end_date']}")
            id += 1


def load_tasks():
    #some try except for learning purposes lol
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                task_data = line.strip().split(',')
                tasks.append({"name": task_data[0], "end_date": task_data[1]})
    except FileNotFoundError:
        print("File not found")
        pass


def remove_task():
    display_tasks()
    if not tasks:
        return
    try:
        task_index = int(input("Enter the index of the task to remove: "))
        if 1 <= task_index <= len(tasks):
            removed_task = tasks.pop(task_index - 1)
            print(f"Task '{removed_task['name']}' removed successfully.")
            save_tasks()
        else:
            print("Invalid index. Please enter a valid index.")
    except ValueError:
        print("Invalid input. Please enter a valid index.")


def edit_task():
    display_tasks()
    if not tasks:
        return

    try:
        task_index = int(input("Enter the index of the task to edit: "))
        if 1 <= task_index <= len(tasks):
            selected_task = tasks[task_index - 1]

            print("What do you want to edit?")
            print("1. Task Name")
            print("2. End Date")
            edit_choice = input("Enter your choice: ")

            if edit_choice == '1':
                new_name = input("Enter new task name: ")
                selected_task['name'] = new_name
            elif edit_choice == '2':
                new_date = input("Enter new end date (YYYY-MM-DD): ")
                selected_task['end_date'] = new_date
            else:
                print("Invalid choice.")
                return

            print(f"Task {task_index} edited successfully.")
            save_tasks()
        else:
            print("Invalid index. Please enter a valid index.")
    except ValueError:
        print("Invalid input. Please enter a valid index.")


def clear_tasks():
    confirmation = input("Are you sure you want to clear the task list? (y/n): ")
    if confirmation.lower() == 'y':
        tasks.clear()
        save_tasks()
        print("Task list cleared.")
    else:
        print("Task list not cleared.")


def task_done():
    display_tasks()
    if not tasks:
        return
    try:
        task_index = int(input("Enter the index of the task done: "))
        if 1 <= task_index <= len(tasks):
            done_task = tasks.pop(task_index - 1)
            save_tasks()

            with open("completedtasks.txt", "a") as file:
                file.write(f"{done_task['name']},{done_task['end_date']}\n")

            print(f"Task '{done_task['name']}' marked as done.")
        else:
            print("Invalid index. Please enter a valid index.")
    except ValueError:
        print("Invalid input. Please enter a valid index.")


def show_completed_tasks():
    try:
        with open("completedtasks.txt", "r") as file:
            completed_tasks = file.readlines()
            if completed_tasks:
                print("Completed Tasks:")
                id = 1
                for task in completed_tasks:
                    name, end_date = task.strip().split(',')
                    print(f"{id}. {name} - Due: {end_date}")
                    id += 1
                time.sleep(2)
                try:
                    with open("grats.txt", "r", encoding="utf-8") as file2:  # Decorations for mood boost stored in grats.txt
                        art = file2.read()
                        print(art)
                    time.sleep(2)
                except FileNotFoundError:
                    pass
            else:
                print("No completed tasks.")
    except FileNotFoundError:
        print("No completed tasks.")


def search_task():
    print("Sorry, brain wasn't braining so I gave up after a long fight with no results")


def main():
    load_tasks()  # Load tasks from file on start so option 2 works with tasks generated before not just current ones
    while True:
        time.sleep(1)
        print("\nTask List Application:")
        print("~~~~~~~~~~~~~~~~~~~~~")
        print("1. add task")
        print("2. display task list")
        print("3. edit task")
        print("4. search task")
        print("5. task done")
        print("6. remove task")
        print("7. clear list")
        print("8. completed tasks")
        print("9. Exit")
        print("~~~~~~~~~~~~~~~~~~~~~")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_task()
        elif choice == '2':
            display_tasks()
        elif choice == '3':
            edit_task()
        elif choice == '4':
            search_task()
        elif choice == '5':
            task_done()
        elif choice == '6':
            remove_task()
        elif choice == '7':
            clear_tasks()
        elif choice == '8':
            show_completed_tasks()
        elif choice == '9':
            print("Bye bye :,(")
            break
        else:
            print("Invalid choice. Please try again!")


if __name__ == "__main__":
    main()
