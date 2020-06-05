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
        create_tabe = "CREATE TABLE cars(Make text, Model text, Trim text, Year text, Price text, Mileage integer, Engine float, Fuel text, Transmission text, Tax float, Insurance text, MPG integer, KM integer, Acceleration integer, Link text, Id integer primary key)"
        cursor.execute(create_tabe)
        #cursor.execute()


