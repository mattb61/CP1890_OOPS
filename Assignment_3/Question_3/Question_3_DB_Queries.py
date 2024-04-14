import sqlite3

# SQL queries to use user input go here


def read_db():
    """ Executes query to read all items from database. Also returns number of total tasks for length
        variable which is used to check that user input does not exceed amount of tasks. """
    conn = sqlite3.connect('task_list_db.sqlite')
    c = conn.cursor()
    query = "SELECT * FROM Task;"
    c.execute(query)
    rows = c.fetchall()
    conn.close()
    return len(rows)


def add_to_db(task_description:str):
    """ Executes query to add user supplied task based on description with completion defaulted to 0. """
    conn = sqlite3.connect('task_list_db.sqlite')
    c = conn.cursor()
    query = f"""INSERT INTO Task(description, completed) VALUES ('{task_description}', 0);"""
    c.execute(query)
    conn.commit()
    conn.close()

def del_from_db(task_id:int):
    """ Executes query to delete user indicated task from database by task ID. """
    conn = sqlite3.connect('task_list_db.sqlite')
    c = conn.cursor()
    query = f"DELETE FROM Task WHERE taskID = {task_id};"
    c.execute(query)
    conn.commit()
    conn.close()

def complete_task(task_id:int):
    """ Executes query to change indicated task by user from 0 to 1 for completion. ."""
    conn = sqlite3.connect('task_list_db.sqlite')
    c = conn.cursor()
    query = f"UPDATE Task SET completed = 1 WHERE taskID = {task_id};"
    c.execute(query)
    conn.commit()
    conn.close()

def view_db():
    """ Executes query to select all non-completed tasks. """
    conn = sqlite3.connect('task_list_db.sqlite')
    c = conn.cursor()
    query = f"SELECT * FROM Task WHERE completed = 0;"
    c.execute(query)
    rows = c.fetchall()
    conn.close()
    return rows


def view_history():
    """ Executes SQL query to select all tasks where completed equals 1, seleting all
        completed tasks and returns them to be used in user input file. """
    conn = sqlite3.connect('task_list_db.sqlite')
    c = conn.cursor()
    query = f"SELECT * FROM Task WHERE completed = 1;"
    c.execute(query)
    rows = c.fetchall()
    conn.close()
    return rows