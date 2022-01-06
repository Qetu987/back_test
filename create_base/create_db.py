from mysql.connector import connect, Error
from settings import connect_data


class Create_db:
    def __init__(self):
        self.con = connect_data()

    def create_tables(self):
        try:
            with connect(
                host=self.con['host'],
                user=self.con['user'],
                password=self.con['password'],
                database=self.con['database'],
            ) as connection:
                create_servises_table_query = """
                        CREATE TABLE servises(
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            name VARCHAR(100)
                        )
                        """
                create_subservises_table_query = """
                        CREATE TABLE subservises (
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            servis_id INT,
                            name VARCHAR(100),
                            price DECIMAL(10,2),
                            date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                            FOREIGN KEY (servis_id) REFERENCES servises(id) ON DELETE CASCADE
                        )
                        """
                with connection.cursor() as cursor:
                    cursor.execute(create_servises_table_query)
                    cursor.execute(create_subservises_table_query)
            print('[+] tables created is successful')
        except Error as e:
            print(e)

    def create_datebase(self):
        try:
            with connect(
                host=self.con['host'],
                user=self.con['user'],
                password=self.con['password'],
            ) as connection:
                create_db_query = "CREATE DATABASE servises_db CHARACTER SET utf8 COLLATE utf8_general_ci;"
                with connection.cursor() as cursor:
                    cursor.execute(create_db_query)
            print('[+] database created is successful')
        except Error as e:
            print(e)

    def set_data(self):
        try:
            with connect(
                host=self.con['host'],
                user=self.con['user'],
                password=self.con['password'],
                database=self.con['database'],
            ) as connection:
                sql_servises = "INSERT INTO servises (name) VALUES (%s)"
                val_servises =[
                    ('first',),
                    ('second',),
                    ('third',),
                ]
                sql_sebservises = "INSERT INTO subservises (servis_id, name, price) VALUES (%s, %s, %s)"
                val_sebservises = [
                    (1, 'BMW', 30000.00),
                    (1, 'Mersedes', 35999.99),
                    (1, 'Pagani', 49999.99),
                    (2, 'Acura', 20000.00),
                    (2, 'Volkswagen', 23000.00),
                    (2, 'Volvo', 19700.85),
                    (2, 'Jeep', 30000.00),
                    (2, 'Dodge', 19999.99),
                    (3, 'Daewoo', 3000.00),
                    (3, 'Citroen', 8000.00),
                    (3, 'Renault', 4500.00),
                    (3, 'Chery', 7000.00),

                ]
                with connection.cursor() as cursor:
                    cursor.executemany(sql_servises, val_servises)
                    cursor.executemany(sql_sebservises, val_sebservises)
                    connection.commit()
            print('[+] data set successful')
        except Error as e:
            print(e)

    def create_db(self):
        self.create_datebase()
        self.create_tables()
        self.set_data()


cr = Create_db()
cr.create_db()