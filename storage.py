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


