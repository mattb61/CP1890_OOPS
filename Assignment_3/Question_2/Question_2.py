"""
Assignment 3

Question 2 - Main User Interface
"""
import Question_2_Functions as Func


def title_menu():
    print("Player Manager")
    print("COMMAND MENU\nview - View players")
    print("add - Add a player\ndel - Delete a player\nexit - Exit program")


def main():
    title_menu()
    while True:
        command = input("\nCommand: ").lower()
        if command == "view":
            Func.view_players()
            command = input("\nCommand: ").lower()
        elif command == "add":
            Func.add_player()
            command = input("\nCommand: ").lower()
        elif command == "del":
            Func.delete_player()
            command = input("\nCommand: ").lower()
        elif command == "exit":
            break
        else:
            print("\nInvalid command, try again.")
            command = input("Command: ").lower()
    print("Bye!")


if __name__ == "__main__":
    main()
