"""
Assignment 3

Question 2 - Main User Interface.
"""
import Question_2_Functions as Func


def title_menu():
    print("Player Manager")
    print(f"\nCOMMAND MENU\n{'view':>6} - View players")
    print(f"{'add':>6} - Add a player\n{'del':>6} - Delete a player")
    print(f"{'update':>6} - Update a player's stats\n{'exit':>6} - Exit program\n")


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
        elif command == "update":
            Func.update_stats()
            print("")
        elif command == "exit":
            break
        else:
            print("\nInvalid command, try again.")
    print("Bye!")


if __name__ == "__main__":
    main()
