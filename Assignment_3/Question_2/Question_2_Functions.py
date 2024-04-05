"""
Assignment 3

Question 2 - Functions.
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
    wins = int(input("Wins: "))
    losses = int(input("Losses: "))
    ties = int(input("Ties: "))

    Q2_sql.add(name, wins, losses, ties)

    print(f"{name} was added to database.")
