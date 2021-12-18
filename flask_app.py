from flask import Flask, request, jsonify
from DBTemp import DBTemp


app = Flask(__name__)


readings = DBTemp()


my_header = {
    'Content-Type': 'application/json'
    }

@app.route('/api/home/', methods=['GET'])
def home():
    return jsonify(readings.select_all_readings())


@app.route('/api/home/<int:readingid>', methods=['GET'])
def get_by_id(readingid):

    my_get_by = readings.select_reading(readingid)

    return jsonify(my_get_by)


@app.route('/api/home/<path:duration>/<int:number>', methods=['GET'])
def last_specified(duration, number):

    between = readings.between_dates(duration, number)

    return jsonify(between)


@app.route('/api/home/delete/<int:readingid>', methods=['GET','DELETE'])
def delete_by_id(readingid):
    readings.delete_reading(readingid)
    return jsonify(readings.select_all_readings())


@app.route('/api/home/create/', methods=['POST'])
def create_reading():
    content = request.get_json()
    readings.insert_reading(content['rasp_id'], content['reading_time'], content['sensor_value'], content['type_id'], content['unit_id'])
    return request.get_json()