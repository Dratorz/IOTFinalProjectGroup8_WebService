from DB import DB



class DBTemp:

    dta = DB()

    def select_all_readings(self):
        return self.dta.execute_select_query("reading")

    def select_reading(self, readingid: int):
        return self.dta.execute_select_query("reading", params={'reading_id': readingid})

    def insert_reading(self, raspberryID: str, readingTime: str, sensorValue: float, typeID: int, unitID: int):
        return self.dta.create_new_query("reading", raspberryID, readingTime, sensorValue, typeID, unitID)

    def delete_reading(self, readingid: int):
        return self.dta.execute_delete_query("reading", "reading_id", readingid)

    def between_dates(self, durationType: str, numberSpec: int):
        return self.dta.last_specified_duration('reading', durationType, numberSpec)