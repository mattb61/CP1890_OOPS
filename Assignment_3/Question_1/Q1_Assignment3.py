import csv, sqlite3


def file_name_entires():
    """
    Obtains user inputs.
    """
    csv_filename = input("CSV File:\t") # customers.csv
    db_filename = input("DB file:  \t") # customers.sqlite
    table_name = input("Table name: ")  # Customer
    return csv_filename, db_filename, table_name


def read_file(csv_filename):
    """
    Reads specified CSV file.
    """
    rows = []
    
    try:
        with open(csv_filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                rows.append(row)
    except FileNotFoundError:
        print(f'\nFile "{csv_filename}" could not be found.')
    finally:
        return rows


def connect_to_db(filename, table, rows):
    """
    Connects to specified database and replaces specified table data with data from 
    """
    num = 0
    
    try:
        conn = sqlite3.connect(f'{filename}')
        c = conn.cursor()
        query = f"delete from {table};"
        c.execute(query)
        for row in rows[1:]:
            c.execute(f"INSERT INTO {table} (firstName, lastName, companyName, address, city, state, zip) VALUES ('{row[0]}', '{row[1]}', '{row[2]}', '{row[3]}', '{row[4]}', '{row[5]}', '{row[6]}');")
            num += 1
        conn.commit()
        conn.close()
    except:
        print(f'\nDatabase "{filename}" or Table "{table}" could not be found.')
    finally:
        return num

if __name__ == "__main__":
    print("Customer Data Importer\n")
    
    csvfile, dbfile, table = file_name_entires()
    rows = read_file(csvfile)
    num = connect_to_db(dbfile, table, rows)
    
    print("\nAll old rows deleted from Customer table")
    print(f"{num} row(s) inserted into Customer table")
