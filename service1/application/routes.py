from application import app
from flask import render_template
import requests

@app.route('/')
def index():
    brands = requests.get('http://service2:5000/brand').text
    return render_template('home.html', brands = brands)