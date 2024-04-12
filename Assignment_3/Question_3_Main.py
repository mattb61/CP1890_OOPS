import Question_3_User_Input as Q3UI

def title():
    print("Task List")
    print()

def command_menu():
    print("COMMAND MENU")
    print("view - View pending tasks")
    print("history - View completed tasks")
    print("add - Add a task")
    print("complete - Complete a task")
    print("delete - Delete a task")
    print("exit - Exit program")
    print()

def main():
    title()
    command_menu()
    ui = Q3UI.UserInput() # Initializes user input class for user input
    while True:

        command = input("Command: ")

        if command.lower() == "view":
            ui.view_tasks()
        elif command.lower() == "history":
            ui.view_history()
        elif command.lower() == "add":
            ui.add_task()
        elif command.lower() == "complete":
            ui.complete_task()
        elif command.lower() == "delete":
            ui.del_task()
        elif command.lower() == "exit":
            print()
            print("Bye!")
            break
        else:
            print("Command does not exist. Please try again.")


if __name__ == "__main__":
    main()