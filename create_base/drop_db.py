from mysql.connector import connect, Error


try:
    with connect(
        host="localhost",
        user="root",
        password="Gfhf_1_ljrc",
    ) as connection:
        show_db_query = "DROP DATABASE servises_db"
        with connection.cursor() as cursor:
            cursor.execute(show_db_query)
            for db in cursor:
                print(db)
except Error as e:
    print(e)