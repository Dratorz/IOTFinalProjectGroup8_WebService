# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request, jsonify
import requests
from DBTemp import DBTemp


app = Flask(__name__)


readings = DBTemp()


my_header = {
    'Content-Type': 'application/json'
    }

@app.route('/')
def hello_world():
    return jsonify(readings.select_all_readings())


@app.route('/<int:readingid>', methods=['GET'])
def get_by_id(readingid):

    my_get_by = readings.select_reading(readingid)

    return jsonify(my_get_by)


@app.route('/delete/<int:readingid>', methods=['GET','DELETE'])
def delete_by_id(readingid):
    readings.delete_reading(readingid)
    return jsonify(readings.select_all_readings())


@app.route('/create/', methods=['POST'])
def create_reading():
    content = request.get_json()
    readings.insert_reading(content['Humidity'], content['Celsius'], content['Fahrenheit'], content['Time'])
    return request.get_json()
