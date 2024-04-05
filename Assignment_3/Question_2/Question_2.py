"""
Assignment 3

Question 2 - Main User Interface.
"""
import Question_2_Functions as Func


def title_menu():
    print("Player Manager\n")
    print("COMMAND MENU\nview - View players")
    print("add - Add a player\ndel - Delete a player\nexit - Exit program\n")


def main():
    title_menu()
    while True:
        command = input("Command: ").lower()
        if command == "view":
            Func.view_players()
            print("")
        elif command == "add":
            Func.add_player()
            print("")
        elif command == "del":
            Func.del_player()
            print("")
        elif command == "exit":
            break
        else:
            print("\nInvalid command, try again.")
    print("Bye!")


if __name__ == "__main__":
    main()
