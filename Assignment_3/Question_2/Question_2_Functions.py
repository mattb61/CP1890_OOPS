"""
Assignment 3

Question 2 - Python Functions / Classes.
"""

import Question_2_SQL as Q2_sql
from dataclasses import dataclass


@dataclass
class Player:
    name: str
    wins: int
    losses: int
    ties: int

    @property
    def games(self):
        return self.wins + self.losses + self.ties

    def update_stats(self, name: str, wins: int, losses: int, ties: int):
        Q2_sql.update(name, wins, losses, ties)

        print(f"{name}'s stats were updated.")

        self.wins = wins
        self.losses = losses
        self.ties = ties


@dataclass
class PlayerList:
    players: list

    def create(self):
        rows = Q2_sql.view()
        for row in rows:
            new = Player(str(row[1]), int(row[2]), int(row[3]), int(row[4]))
            self.players.append(new)

    def add_player(self, name: str, wins: int, losses: int, ties: int):
        name = name.title()

        Q2_sql.add(name, wins, losses, ties)

        new_player = Player(name, wins, losses, ties)

        self.players.append(new_player)
        print(f"{name} was added to database.")

    def del_player(self, player_name: str):
        player_name = player_name.title()
        for player in self.players:
            if player.name == player_name:
                self.players.remove(player)

        Q2_sql.delete(player_name)
        print(f"{player_name} was deleted from database.")

    def update_player(self, player_name: str, wins: int, losses: int, ties: int):
        check = 0
        player_name = player_name.title()
        for player in self.players:
            if player.name == player_name:
                player.update_stats(player_name, wins, losses, ties)
                check = 1

        if check == 0:
            print(f"{player_name} not found in database.")

    def view_players(self):
        self.players = []
        self.create()
        print(f"{'Name':<20}{'Wins':<4}    {'Losses':<6}    {'Ties':<4}    {'Games':<5}")
        print('-' * 60)
        for player in self.players:
            print(f"{player.name:<20}{player.wins:4}    {player.losses:6}    {player.ties:4}    {player.games:5}")


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


player_list = PlayerList([])
player_list.create()
