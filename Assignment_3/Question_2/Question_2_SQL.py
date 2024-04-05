"""
Assignment 3

Question 2 - SQL related functions/commands.
"""

import sqlite3


def view():
    conn = sqlite3.connect('Question2_Supporting_Files/player_db.sqlite')
    c = conn.cursor()
    c.execute("SELECT * from Player order by wins desc;")
    rows = c.fetchall()
    conn.close()

    return rows


def add(player_name, player_wins, player_losses, player_ties):
    query = f"""INSERT INTO Player (name, wins, losses, ties)
    VALUES ('{player_name}', '{player_wins}', '{player_losses}', '{player_ties}')
    """

    conn = sqlite3.connect('Question2_Supporting_Files/player_db.sqlite')
    c = conn.cursor()
    c.execute(query)
    conn.commit()
    conn.close()


def delete(player_name):
    query = f"DELETE from Player WHERE name = '{player_name}'"

    conn = sqlite3.connect('Question2_Supporting_Files/player_db.sqlite')
    c = conn.cursor()
    c.execute(query)
    conn.commit()
    conn.close()
