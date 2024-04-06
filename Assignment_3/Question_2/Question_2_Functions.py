"""
Assignment 3

Question 2 - Python functions.
"""

import Question_2_SQL as Q2_sql


def view_players():
    rows = Q2_sql.view()
    print(f"{'Name':<20}{'Wins':<4}    {'Losses':<6}    {'Ties':<4}    {'Games':<5}")
    print('-' * 60)
    for row in rows:
        games = int(row[2]) + int(row[3]) + int(row[4])
        print(f"{row[1]:<20}{row[2]:4}    {row[3]:6}    {row[4]:4}    {games:5}")


def del_player():
    player_name = input("Name: ").title()
    Q2_sql.delete(player_name)
    print(f"{player_name} was deleted from database.")


def add_player():
    name = input("Name: ").title()
    wins, losses, ties = get_int()

    Q2_sql.add(name, wins, losses, ties)

    print(f"{name} was added to database.")


def update_stats():
    players = Q2_sql.player_list()
    cont = 0

    player_name = input("Name: ").title()
        
    for player in players:
        if player == player_name:
            cont = 1
        
    if cont != 1:
        print(f"{player_name} not found in database.")
    else:
        player_wins, player_losses, player_ties = get_int()
            
        Q2_sql.update(player_name, player_wins, player_losses, player_ties)
            
        print(f"{player_name}'s stats were updated.")


def get_int():
    while True:
        try:
            player_wins = int(input("Wins: "))
            if player_wins < 0:
                print("Cannot accept negative values.\n")
            else:
                break
        except ValueError:
            print("Invalid integer.\n")
            continue
    while True:
        try:
            player_losses = int(input("Losses: "))
            if player_losses < 0:
                print("Cannot accept negative values.\n")
            else:
                break
        except ValueError:
            print("Invalid integer.\n")
    while True:
        try:
            player_ties = int(input("Ties: "))
            if player_ties < 0:
                print("Cannot accept negative values.\n")
            else:
                break
        except ValueError:
            print("Invalid integer.\n")
    return player_wins, player_losses, player_ties
