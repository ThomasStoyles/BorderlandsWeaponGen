from flask import Flask
from flask import request
from application import app
import random as rd 

@app.route('/final', methods=['POST'])
def final():
    overalldamage = 0
    data = request.get_json()
    # manufacturers
    if data['Manufacturer'] == 'Atlas':
        overalldamage += 10
    if data['Manufacturer'] == 'Hyperion':
        overalldamage += 40      
    if data['Manufacturer'] == 'Jakobs':
        overalldamage += 50
    if data['Manufacturer'] == 'Maliwan':
        overalldamage += 45
    if data['Manufacturer'] == 'Anshin':
        overalldamage += 25
    if data['Manufacturer'] == 'Vladof':
        overalldamage += 30
    if data['Manufacturer'] == 'a':
        overalldamage += 430
    if data['Manufacturer'] == 'b':
        overalldamage += 330
    if data['Manufacturer'] == 'c':
        overalldamage += 230
    # rarity 
    if data['rarity'] == 'Common':
        overalldamage += 5
    if data['rarity'] == 'Uncommon':
        overalldamage += 15
    if data['rarity'] == 'Rare':
        overalldamage += 30
    if data['rarity'] == 'Epic':
        overalldamage += 50
    if data['rarity'] == 'Legendary':
        overalldamage += 100
    if data['rarity'] == 'Unknown':
        overalldamage += 250
    if data['rarity'] == 'Pearlescent':
        overalldamage += 150

    return str(overalldamage)
