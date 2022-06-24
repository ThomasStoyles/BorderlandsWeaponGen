from application import app
from flask import render_template
import requests

@app.route('/')
def index():
    Manufacturers = requests.get('http://service2:5000/Manufacturer').text
    raritys = requests.get('http://service3:5000/rarity').text
    finals = requests.post('http://service4:5000/final',json={'Manufacturer':Manufacturers,'rarity':raritys}).text
    return render_template('home.html', Manufacturers = Manufacturers, raritys=raritys, finals=finals)