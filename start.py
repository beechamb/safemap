from flask import Flask, render_template



app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/map')
def mapping():
    return render_template('map.html')

@app.route('/report')
def report():
    return render_template('report.html')