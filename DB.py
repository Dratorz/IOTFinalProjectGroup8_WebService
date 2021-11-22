import mysql.connector


class DB(object):

    def __init__(self):
        try:
            self.config_file = "my.conf"
            self.connect = mysql.connector.connect(option_files = self.config_file)
        except mysql.connector.Error as e:
            print(e)
            self.close()

    def execute_select_query(self, table_name, params=None):
        return_set = []
        cursor = self.connect.cursor(dictionary=True)
        if params is None:
            cursor.execute("SELECT * FROM {}".format(table_name))
        else:
            where_clause = " WHERE " + " AND ".join(['`' + k + '` = %s' for k in params.keys()])
            print(where_clause)

            values = list(params.values())
            print(values)

            sql = "SELECT * FROM {}".format(table_name) + where_clause
            print(sql)

            cursor.execute(sql, values)

        for x in cursor:
            return_set.append(x)

        cursor.close()
        return return_set

    def execute_delete_query(self, table_name, idname, readingid: int):

        cursor = self.connect.cursor(dictionary=True)
        try:
            cursor.execute("DELETE FROM {} WHERE {} ={}".format(table_name, idname, readingid))
        except mysql.connector.Error as e:
            print(e)

        self.connect.commit()
        cursor.close()

    def create_new_query(self, table_name, humidity: float, celsius: float, fahrenheit: float, timereading):

        cursor = self.connect.cursor(dictionary=True)

        cursor.execute("INSERT INTO {} (Humidity, Celsius, Fahrenheit, Time) VALUES({}, {}, {}, \"{}\")".format(table_name, humidity, celsius, fahrenheit, timereading))
        self.connect.commit()
        cursor.close()

