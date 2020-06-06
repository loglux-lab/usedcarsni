import sqlite3

class Storage():
    def __init__(self, file='data.db'):
        self.file=file
    def __enter__(self):
        self.connection = sqlite3.connect(self.file)
#        self.connection.row_factory = sqlite3.Row
        return self.connection.cursor()
    def __exit__(self, type, value, traceback):
        self.connection.commit()
        self.connection.close()


class Operations():
    def __init__(self):
        self.cars_table = """CREATE TABLE IF NOT EXISTS cars(
        Make text, 
        Model text, 
        Trim text, 
        Year text, 
        Price text, 
        Mileage integer, 
        Engine float, 
        Fuel text, 
        Transmission text, 
        Tax float, 
        Insurance text, 
        MPG integer, 
        KM integer, 
        Acceleration integer, 
        Link text, 
        Id integer primary key
        )"""
        self.price_table = """CREATE TABLE IF NOT EXISTS price_watch(
        H_Date text, 
        H_Price real, 
        Id integer,
        UNIQUE (H_Date, H_Price, Id),
        FOREIGN KEY (Id) REFERENCES cars (Id)
        );"""
        self.insert_car =   """INSERT INTO cars (
        Make, 
        Model, 
        Trim, 
        Year, 
        Price, 
        Mileage, 
        Engine, 
        Fuel, 
        Transmission, 
        Tax, 
        Insurance, 
        MPG, 
        KM, 
        Acceleration, 
        Link, 
        Id)  
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?  
        );"""
        self.tasks = []

    def create_tables(self):
        with Storage() as cursor:
            cursor.execute(self.cars_table)
            cursor.execute(self.price_table)

    def insert_tables(self):
        with Storage() as cursor:
            cursor.execute(self.insert_car)


class DB():

    def some_db(self):
        """ START. Adding a record into Database """
        with Storage() as cursor:
            try:
                cursor.execute(self.insert_date,
                               (self.current_date, self.car_description['Price'], self.car_description['Id']))
                cursor.execute(self.insert_car, list(self.car_description.values()))
            except sqlite3.IntegrityError:
                """ TODO: Search Results Web results SQLite IntegrityError: UNIQUE constraint failed:"""
                """ Checkig a previous price and comparsion with a current one """
                # row_check = f"SELECT Price from cars WHERE Id = {self.car_description['Id']}"
                """ How to make a comparison and save a result. """
                cursor.execute(self.row_check, (self.car_description['Id'],))
                previous_price = cursor.fetchone()
                print("Old Price: " + ''.join(previous_price))
                print("Current Price: " + self.car_description['Price'])
                price_difference = int(''.join(previous_price).replace('£', '')) - int(
                    self.car_description['Price'].replace('£', ''))
                print("Price difference: " + str(price_difference))
                if price_difference != 0:
                    cursor.execute(self.update_car, (self.car_description['Price'], self.car_description['Id']))
                """ TODO: create a table for price traking """
                cursor.execute(self.price_select, (self.car_description['Id'],))
                result = cursor.fetchall()
                """ To get a dictionary from the request """
                data = dict(zip([c[0] for c in cursor.description], result[0]))
                print(data)
                print(type(result))
                print(result)

            """ END Database"""


if __name__ == '__main__':
    with Storage() as cursor:
        cars_table = """CREATE TABLE IF NOT EXISTS cars(
        Make text, 
        Model text, 
        Trim text, 
        Year text, 
        Price text, 
        Mileage integer, 
        Engine float, 
        Fuel text, 
        Transmission text, 
        Tax float, 
        Insurance text, 
        MPG integer, 
        KM integer, 
        Acceleration integer, 
        Link text, 
        Id integer primary key
        )"""
        price_table = """CREATE TABLE IF NOT EXISTS price_watch(
        H_Date text, 
        H_Price real, 
        Id integer,
        UNIQUE (H_Date, H_Price, Id),
        FOREIGN KEY (Id) REFERENCES cars (Id)
        );"""
        cursor.execute(cars_table)
        cursor.execute(price_table)
        #cursor.execute()


