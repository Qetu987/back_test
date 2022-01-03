from http.server import BaseHTTPRequestHandler
from mysql.connector import connect, Error
import json


class HttpGetHandler(BaseHTTPRequestHandler):

    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_HEAD(self):
        self._set_headers()

    def get_row_data(self, get_count_query):
        try:
            with connect(
                    host="localhost",
                    user="root",
                    password="Gfhf_1_ljrc",
                    database="servises_db",
            ) as connection:
                with connection.cursor() as row_cursor:
                    row_cursor.execute(get_count_query)
                    data_count = row_cursor.fetchone()[0]
                    return data_count
        except Error as e:
            print(e)

    def get_sebservises_data(self, id):
        try:
            with connect(
                    host="localhost",
                    user="root",
                    password="Gfhf_1_ljrc",
                    database="servises_db",
            ) as connection:
                get_count_query = f"SELECT * FROM subservises WHERE servis_id = {id} ORDER BY price DESC, name ASC"
                with connection.cursor() as row_cursor:
                    row_cursor.execute(get_count_query)
                    data = row_cursor.fetchall()
                    return data
        except Error as e:
            print(e)

    def get_servises_data(self):
        data = None
        try:
            with connect(
                host="localhost",
                user="root",
                password="Gfhf_1_ljrc",
                database="servises_db",
            ) as connection:
                get_servises_table_query = """
                    SELECT * FROM servises
                """
                with connection.cursor() as cursor:
                    cursor.execute(get_servises_table_query)
                    data = cursor.fetchall()
        except Error as e:
            print(e)

        returned_data = []
        for id, value in data:
            get_count_query = f"SELECT count(*) FROM subservises WHERE servis_id = {id}"
            count = self.get_row_data(get_count_query)
            get_count_query = f"SELECT sum(price) FROM subservises WHERE servis_id = {id}"
            sum_item = self.get_row_data(get_count_query)
            returned_data.append((id, str(value) + f'({count})({sum_item})'))
        return returned_data

    def do_GET(self):
        self._set_headers()

        path = self.path
        if path == '/':
            records = self.get_servises_data()
            data = dict()
            for key, value in records:
                data[key] = value
            response = json.dumps(data)
            response = bytes(response, 'utf-8')
            self.wfile.write(response)
        elif path.split('/')[-1].isdigit():
            records = self.get_sebservises_data(path.split('/')[-1])
            data = []
            for item in records:
                item_element = dict()
                item_element['id'] = item[0]
                item_element['servises_id'] = item[1]
                item_element['model'] = item[2]
                item_element['price'] = str(item[3])
                item_element['date'] = str(item[4])
                data.append(item_element)
            response = json.dumps(data)
            response = bytes(response, 'utf-8')
            self.wfile.write(response)
        else:
            self.send_error(404)