class Temperature:
    readingid = 0
    humidity = 0.0
    celsius = 0.0
    fahrenheit = 0.0
    datetime = ""

    def __init__(self, humidity: float, celsius: float, fahrenheit: float, datetime: str):
        self.humidity = humidity
        self.celsius = celsius
        self.fahrenheit = fahrenheit
        self.datetime = datetime
