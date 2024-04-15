import sqlite3, csv
from dataclasses import dataclass

if __name__ == "__main__":
    DB_FILENAME = "sales_database.sqlite"


@dataclass
class Region:
    code: str
    name: str


@dataclass
class Regions:
    RegionList: list

    def add(self, DB_FILENAME):
        conn = sqlite3.connect(DB_FILENAME)
        c = conn.cursor()
        query = "SELECT code, name FROM Region;"
        c.execute(query)
        rows = c.fetchall()
        conn.close()
        
        for row in rows:
            region = Region(row[0], row[1])
            self.RegionList.append(region)
    

@dataclass
class DailySales:
    saleId: int
    amount: float
    date: str
    region: str


def read_list(FILENAME):
    sales_list = []
    with open(str(FILENAME), newline='') as file_handler:
        reader = csv.reader(file_handler)
        for row in reader:
            sales_list.append([float(row[0]), str(row[1]), str(row[2])])
        return sales_list


def add_sales(new_sales, DB_FILENAME):
    for sale in new_sales:
        conn = sqlite3.connect(DB_FILENAME)
        c = conn.cursor()
        query = f"insert into Sales (amount, salesDate, region) values ({sale[0]}, '{sale[1]}', '{sale[2]}')"
        c.execute(query)
        conn.commit()
        conn.close()
    

def add_file(new_data, DB_FILENAME):
    conn = sqlite3.connect(DB_FILENAME)
    c = conn.cursor()
    query = f"insert into ImportedFiles values ('{new_data}')"
    c.execute(query)
    conn.commit()
    conn.close()


def imported_files(DB_FILENAME):
    sales_log = []
    conn = sqlite3.connect(DB_FILENAME)
    c = conn.cursor()
    query = "SELECT fileName FROM ImportedFiles;"
    c.execute(query)
    rows = c.fetchall()
    conn.close()
    for row in rows:
        sales_log.append(row)
    return sales_log


def read_db(DB_FILENAME):
    conn = sqlite3.connect(DB_FILENAME)
    c = conn.cursor()
    query = "SELECT * FROM Sales;"
    c.execute(query)
    rows = c.fetchall()
    conn.close()
    
    sales = []
    
    for row in rows:
        sale = DailySales(row[0], row[1], row[2], row[3])
        sales.append(sale)
    
    return sales
