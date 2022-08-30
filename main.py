from flask import Flask, jsonify, request
from escpos import *

app = Flask(__name__)
p = printer.Usb(0x0416, 0x5011, 0, 0x81, 0x03)


@app.route('/')
def index():
    return "Hey there! This is Alli's Thermal Printer, Volcano. Please do a real API call you stupid bitch"


@app.route('/erupt', methods=['POST'])
def erupt():
    r = request.get_json()
    type = r.get('type')
    if (type == 'text'):
        p.text(r.get('payload'))
        return '200: printing...', 200
    if (type == 'image'):
        p.image(r.get('payload'))
        return '200: printing...', 200
    else:
        return '404: Not a valid type', 400


if __name__ == '__main__':
    app.run(debug=True)
