import mysql.connector


class DB(object):

    def __init__(self):
        try:
            self.config_file = "my.conf"
            self.connect = mysql.connector.connect(option_files=self.config_file)
        except mysql.connector.Error as e:
            print(e)
            self.close()

    def execute_select_query(self, table_name, params=None):
        return_set = []
        cursor = self.connect.cursor(dictionary=True)

        column_names = "a.reading_id, a.rasp_id, a.reading_time, a.sensor_value, b.type_id, b.type_name, " \
                       "f.unit_id, f.unit_name, f.unit"

        tbl1 = "type"
        tbl1_id = "type_id"
        tbl2 = "unit"
        tbl2_id = "unit_id"
        order_by = "reading_id"

        if params is None:

            cursor.execute(
                "SELECT {} FROM {} a JOIN {} b ON a.{} = b.{} JOIN {} f ON a.{} = f.{} ORDER BY {} LIMIT 15".format(
                    column_names, table_name, tbl1, tbl1_id, tbl1_id, tbl2, tbl2_id, tbl2_id, order_by))

        else:
            where_clause = " WHERE " + " AND ".join(['`' + k + '` = %s' for k in params.keys()])
            print(where_clause)

            values = list(params.values())
            print(values)

            sql = "SELECT {} FROM {} a JOIN {} b ON a.{} = b.{} JOIN {} f ON a.{} = f.{}".format(column_names,
                                                                                                 table_name, tbl1,
                                                                                                 tbl1_id, tbl1_id, tbl2,
                                                                                                 tbl2_id,
                                                                                                 tbl2_id) + where_clause
            print(sql)

            print(sql + where_clause)
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

    def create_new_query(self, table_name, raspberryID: str, readingTime: str, sensorValue: float, typeID: int,
                         unitID: int):

        cursor = self.connect.cursor(dictionary=True)
        print((
                  "INSERT INTO {} (rasp_id, reading_time, sensor_value, type_id, unit_id) VALUES(\"{}\", \"{}\", {}, {}, {})".format(
                      table_name, raspberryID, readingTime, sensorValue, typeID, unitID)))
        cursor.execute(
            "INSERT INTO {} (rasp_id, reading_time, sensor_value, type_id, unit_id) VALUES(\"{}\", \"{}\", {}, {}, {})".format(
                table_name, raspberryID, readingTime, sensorValue, typeID, unitID))
        self.connect.commit()
        cursor.close()

    def last_specified_duration(self, table_name, durationType: str, numberSpec: int):

        return_set = []
        cursor = self.connect.cursor(dictionary=True)

        column_names = "a.reading_id, a.rasp_id, a.reading_time, a.sensor_value, b.type_id, b.type_name, " \
                       "f.unit_id, f.unit_name, f.unit"

        tbl1 = "type"
        tbl1_id = "type_id"
        tbl2 = "unit"
        tbl2_id = "unit_id"
        where_clause = "a.reading_time >=NOW() + INTERVAL - {} {}".format(numberSpec, durationType)
        order_by = "reading_id"
        print("SELECT {} FROM {} a JOIN {} b ON a.{} = b.{} JOIN {} f ON a.{} = f.{} WHERE {} ORDER BY {} LIMIT 15".format(
                column_names, table_name, tbl1, tbl1_id, tbl1_id, tbl2, tbl2_id, tbl2_id, where_clause, order_by))
        cursor.execute(
            "SELECT {} FROM {} a JOIN {} b ON a.{} = b.{} JOIN {} f ON a.{} = f.{} WHERE {} ORDER BY {} LIMIT 15".format(
                column_names, table_name, tbl1, tbl1_id, tbl1_id, tbl2, tbl2_id, tbl2_id, where_clause, order_by))

        for x in cursor:
            return_set.append(x)

        cursor.close()
        return return_set
