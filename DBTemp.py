from DB import DB



class DBTemp:

    dta = DB()

    def select_all_readings(self):
        return self.dta.execute_select_query("TemperatureReadings")

    def select_reading(self, readingid: int):
        return self.dta.execute_select_query("TemperatureReadings", params={'ReadingID': readingid})

    def insert_reading(self, humidity: float, celsius: float, fahrenheit: float, timeReading: str):
        return self.dta.create_new_query("TemperatureReadings", humidity, celsius, fahrenheit, timeReading)

    def delete_reading(self, readingid: int):
        return self.dta.execute_delete_query("TemperatureReadings", "ReadingID", readingid)
