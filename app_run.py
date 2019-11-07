from flask import *
from datetime import datetime
import Calculator as calculator
app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    data = "Deploying a Flask App To Heroku"
    return render_template('index.html')

@app.route('/r')
def r():
    a = num(request.args.get('a'))
    return str(calculator.r(a))


def num(s):
    try:
        return int(s)
    except ValueError:
        return float(s)

if __name__ == '__main__':
    app.run(debug=True)