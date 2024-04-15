import Q5_Classes as sic


DB_FILENAME = "sales_database.sqlite"


def menu():
    """
    Prints Command Menu.
    """
    print("\nCOMMAND MENU\nview - View all sales\nadd - Add Sales")
    print("import - import data from csv file")
    print("menu - Show menu\nexit - Exit program")
    return


def day_input(month):
    """
    Gets and verifies user input for day.
    
    Parameters
    ----------
    month : Int
        Month of sale.

    Returns
    -------
    day : Int
        Day of sale.
    """
    if month == 4 or month == 6 or month == 9 or month == 11:
        day = int(input("Day(1-30):\t\t"))
        if day < 1 or day > 30:
            print("Day should be 1-30.\n")
            day = day_input(month)
    elif month == 2:
        day = int(input("Day(1-28):\t\t"))
        if day < 1 or day > 28:
            print("Day should be 1-28.\n")
            day = day_input(month)
    else:
        day = int(input("Day(1-31):\t\t"))
        if day < 1 or day > 31:
            print("Day should be 1-31.\n")
            day = day_input(month)
    return day


def view():
    """
    Prints out all sales.
    """
    sales = sic.read_db(DB_FILENAME)
    
    total = 0
    if sales == False:
        print("No sales to view.\n")
    else:
        print("\t\t\tDate\t\t\tQuarter\t\t\tRegion\t\t\tAmount")
        print('-' * 70)
        for sale in sales:
            print(f"\n{sale.saleId}.\t\t\t{sale.date}\t\t{quarter(sale.date)}\t\t\t\t{sale.region}\t\t\t\t${sale.amount:.2f}")
            total = float(total) + float(sale.amount)
        print('-' * 70)
        print(f"TOTAL:\t\t\t\t\t\t\t\t\t\t\t\t\t\t${total:.2f}")


def get_region():
    regionlist = sic.Regions([])
    regionlist.add(DB_FILENAME)
    
    codes = []
    for region in regionlist.RegionList:
        codes.append(region.code)

    while True:
        region = input("Enter region code: ").lower()
        if region in codes:
            break
        else:
            print("\nRegion not found, region should be one of the following:")
            for region in regionlist.RegionList:
                print(f"{region.code} = {region.name}")
            print("")
            continue
    return region


def add():
    """
    Adds new sale to database.
    """
    single_digit = (1, 2, 3, 4, 5, 6, 7, 8, 9)
    
    #Amount:
    amount = float(input("Amount:\t\t\t"))
    while amount <= 0:
        print("Sales amount must be greater than zero.")
        amount = float(input("\nAmount:\t\t\t"))
    
    #Date:
    year = int(input("Year:\t\t\t"))
    while year < 1900 or year > 3000:
        print("Year must bebetween 1900 and 3000.\n")
        year = int(input("Year (1900-3000):\t\t\t"))
        
    month = int(input("Month (1-12):\t"))
    while month < 1 or month > 12:
        print("Month must be between 1 and 12.\n")
        month = int(input("Month (1-12):\t"))
    if month in single_digit:
        month = f"0{month}"
    
    day = day_input(month)
    if day in single_digit:
        day = f"0{day}"
    
    date = f"{year}-{month}-{day}"
    
    #Region:
    region = get_region()
    
    new = [[amount, date, region]]
    
    sic.add_sales(new, DB_FILENAME)
    print(f"Sales data for {year}-{month}-{day} has been added.")


def import_data():
    """
    This function imports sales data from a csv file.
    """
    prior_data = sic.imported_files(DB_FILENAME)
    new_data = input("Enter name of file to import: ")
    if new_data in prior_data:
        print(f"File '{new_data}' has already been imported.")
    else:
        import_data = sic.read_list(new_data)
        sic.add_sales(import_data, DB_FILENAME)
        sic.add_file(new_data, DB_FILENAME)


def quarter(date):
    """
    Parameters
    ----------
    month : INT
        Month of sale.

    Returns
    -------
    quarter : INT
        Quarter of sale.
    """
    month = int(date[6:7])
    
    if month >= 1 and month < 4:
        quarter = 1
    elif month >= 4 and month < 7:
        quarter = 2
    elif month >= 7 and month < 10:
        quarter = 3
    elif month >= 10 and month < 13:
        quarter = 4
    return quarter


def logic():
    """
    
    """
    cmd = input("\nPlease enter a command: ")

    cont = 'x'
    while cont == 'x':
        if cmd.lower() == "view":
            view()
            cmd = input("\nPlease enter a command: ")
        elif cmd.lower() == "add":
            add()
            cmd = input("\nPlease enter a command: ")
        elif cmd.lower() == "import":
            import_data()
            cmd = input("\nPlease enter a command: ")
        elif cmd.lower() == "menu":
            menu()
            cmd = input("\nPlease enter a command: ")
        elif cmd.lower() == "exit":
            cont = 'a'
        else:
            print("Invalid Command. Please try again.")
            menu()
            cmd = input("\nPlease enter a command: ")
    return


def main():
    """
    Calls all functions.
    """
    print("SALES DATA IMPORTER\n")

    menu()
    logic()
    
    print("\nBye!")


if __name__ == "__main__":
    main()
