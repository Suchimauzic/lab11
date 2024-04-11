from flask import Flask
from flask import request
from math import sin as msin, cos as mcos, tan as mtan, pi

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Flask!'

def to_int(a, b):
    return [int(a), int(b)]

def to_float(a, b):
    return [float(a), float(b)]

@app.route('/add')
def add():
    fir = request.args.get('fir')
    sec = request.args.get('sec')
    td = request.args.get('td')

    if (td == "int"):
        fir, sec = to_int(fir, sec)
    elif (td == "float"):
        fir, sec = to_float(fir, sec)
    else:
        return 'Error! Bad convert'

    return str(fir + sec)

@app.route('/sub')
def sub():
    fir = request.args.get('fir')
    sec = request.args.get('sec')
    td = request.args.get('td')

    if (td == "int"):
        fir, sec = to_int(fir, sec)
    elif (td == "float"):
        fir, sec = to_float(fir, sec)
    else:
        return 'Error! Bad convert'

    return str(fir - sec)

@app.route('/mul')
def mul():
    fir = request.args.get('fir')
    sec = request.args.get('sec')
    td = request.args.get('td')

    if (td == "int"):
        fir, sec = to_int(fir, sec)
    elif (td == "float"):
        fir, sec = to_float(fir, sec)
    else:
        return 'Error! Bad convert'

    return str(fir * sec)

@app.route('/div')
def div():
    fir = request.args.get('fir')
    sec = request.args.get('sec')
    td = request.args.get('td')
    if (sec == '0'):
        return 'Division by 0'

    if (td == "int"):
        fir, sec = to_int(fir, sec)
        return str(fir // sec)
    elif (td == "float"):
        fir, sec = to_float(fir, sec)
        return str(fir / sec)
    else:
        return 'Error! Bad convert'

# From degree to radian
def deg_to_rad(a):
    return a * pi / 180

@app.route('/sin')
def sin():
    fir = request.args.get('fir')
    mode = request.args.get('mode')
    td = request.args.get('td')

    if (td == 'int'):
        fir = int(fir)
    elif (td == 'float'):
        fir = float(fir)
    else:
        return 'Error! Bad convert'

    if (mode == 'degree'):
        fir = deg_to_rad(fir)

    return str(msin(fir))

@app.route('/cos')
def cos():
    fir = request.args.get('fir')
    mode = request.args.get('mode')
    td = request.args.get('td')

    if (td == 'int'):
        fir = int(fir)
    elif (td == 'float'):
        fir = float(fir)
    else:
        return 'Error'

    if (mode == 'degree'):
        fir = deg_to_rad(fir)

    return str(mcos(fir))

@app.route('/tan')
def tan():
    fir = request.args.get('fir')
    mode = request.args.get('mode')
    td = request.args.get('td')

    if (td == 'int'):
        fir = int(fir)
    elif (td == 'float'):
        fir = float(fir)
    else:
        return 'Input type'

    if (mode == 'degree'):
        if (fir == 90 or fir == 270):
            return 'Error!!'
        fir = deg_to_rad(fir)
    elif (mode == 'radian'):
        if (fir == pi / 2 or fir == (3 * pi) / 2):
            return 'Error!!'
    else:
        return 'Input mode'

    return str(mtan(fir))

@app.route('/sqrt')
def sqrt():
    fir = request.args.get('fir')
    td = request.args.get('td')

    if (int(fir) < 0):
        return 'Error! Root of negative number'

    if (td == 'int'):
        return str(int(int(fir) ** 0.5))
    elif (td == 'float'):
        return str(float(fir) ** 0.5)
    else:
        return 'Error! Bad convert'

@app.route('/pow')
def pow():
    fir = request.args.get('fir')
    sec = request.args.get('sec')
    td = request.args.get('td')

    if (td == 'int'):
        return str(int(fir) ** int(sec))
    elif (td == 'float'):
        try:
            return str(float(fir) ** float(sec))
        except:
            return 'Error! Bad numbers!'
    else:
        return 'Error! Bad convert'
