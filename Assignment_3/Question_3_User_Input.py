import Question_3_DB_Queries as Q3_sql
from dataclasses import dataclass
import sqlite3

conn = sqlite3.connect('task_list_db.sqlite')
c = conn.cursor()
# User input functions go here

length = Q3_sql.read_db() # Variable to store the amount of tasks to ensure error handling of inputted task IDs that exceed number of tasks

@dataclass
class Task:
# Possibly redundant class, leaving it in in case it breaks something.

    task_id:int = 1
    description:str = ""
    completed:int = 0

    @property
    def task(self):
        return self.task_id, self.description, self.completed


@dataclass
class UserInput:

    def view_tasks(self):
        """ Reads unfinished tasks pulled from view_db query in the Queries file
            and lists them with enumeration. """
        rows = Q3_sql.view_db()
        for i, rows in enumerate(rows, start=1):
            print(f"{i}. {rows[1]}")

    def view_history(self):
        """ Reads finished tasks pulled from view_history query in the Queries file
            and lists them with enumeration. """
        rows = Q3_sql.view_history()
        for i, rows in enumerate(rows, start=1):
            print(f"{i}. {rows[1]} (DONE!)")

    def add_task(self):
        """Takes in user input and feeds it to add_to_db query in the Queries file"""
        task_description = input("Description: ")
        Q3_sql.add_to_db(task_description)

    def del_task(self):
        """ Takes in user input and feeds it to delete query in the Queries file after checking if integer
            is larger than 0, a positive number, or if it's an integer at all. """
        while True:
            try:
                task_id = int(input("Number: "))
                if task_id < 1 or task_id > length:
                    print("Invalid integer. Task ID either less than 1 or exceeds amount of tasks.")
                else:
                    Q3_sql.del_from_db(task_id)
                    break
            except ValueError:
                print("Integers only. Please try again.")

    def complete_task(self):
        """ Takes in user input integer and feeds it to the complete_task query in the Queries file to delete
            task in database as long as task ID exists. """
        while True:
            try:
                task_id = int(input("Number: "))
                if task_id < 1 or task_id > length:
                    print("Invalid integer. Task ID either less than 1 or exceeds amount of tasks.")
                else:
                    Q3_sql.complete_task(task_id)
                    break
            except ValueError:
                print("Integers only. Please try again.")