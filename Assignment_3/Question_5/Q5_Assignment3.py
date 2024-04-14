import sqlite3
from Q5_Classes import Region, DailySales, RegionsList


DB_FILENAME = "sales_database.sqlite"

def connect():
    conn = sqlite3.connect(DB_FILENAME)
    conn.row_factory = sqlite3.Row
    return conn


def close(conn):
    conn.close()
    print("Closed")


def create_table(conn):
    cur = conn.cursor()
    query = "CREATE TABLE IF NOT EXISTS Sales (id INTEGER PRIMARY KEY AUTOINCREMENT, amount REAL, salesDate TEXT, region TEXT)"
    cur.execute(query)
    conn.commit()
    query = "CREATE TABLE IF NOT EXISTS Region (code TEXT PRIMARY KEY, name TEXT)"
    cur.execute(query)
    conn.commit()
    query = "CREATE TABLE IF NOT EXISTS ImportedFiles (fileName TEXT PRIMARY KEY)"
    cur.execute(query)
    conn.commit()
    print("Tables Created")


# def create_sales(conn):
#     cur = conn.cursor()
#     query = "INSERT INTO Sales VALUES (?, ?, ?, ?)"
#     sales = ((1, 27.50, '2024-2-1', get_region(conn, 'e')), (2, 14.99, '2021-11-18', get_region(conn, 'w')))
#     for i in range(len(sales)):
#         cur.execute(query, sales[i])
#     conn.commit()


def create_regions():
    new_region = Region()
    RegionsList.append(new_region)


def get_regions(conn):
    cur = conn.cursor()
    for i in RegionsList:
        query = "SELECT Region FROM RegionsList"
        cur.execute(query)


# def create_regions(conn):
#     cur = conn.cursor()
#     query = "INSERT INTO Region VALUES (?, ?)"
#     regions = (('e', 'East'), ('w', 'West'), ('n', 'North'))
#     for i in range(len(regions)):
#         cur.execute(query, regions[i])
#     conn.commit()


# def get_region(conn, region_name):
#     cur = conn.cursor()
#     query = f"SELECT code FROM Region WHERE name = '{region_name}'"
#     cur.execute(query)
#     result = cur.fetchone()
#     if result:
#         return result[0]
#     else:
#         return None
