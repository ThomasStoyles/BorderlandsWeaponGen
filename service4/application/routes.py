from flask import Flask
from flask import request
from application import app
import random as rd 


damagetypes = ['Normal','Fire','Electric','Ice','Corrosive','Sluge','Explosive']

@app.route('/final', methods=['POST'])
def final():
    data = request.get_json()
    Manufacturer = data['Manufacturer']
    rarity = int(data['rarity'])
    if rarity <= 30:
        rareness = "Common"
    elif rarity <= 55:
        rareness = "Uncommon"
    elif rarity <= 75:
        rareness = "Rare"
    elif rarity <= 90:
        rareness = "Epic"
    elif rarity <= 100:
        rareness = "Legendary"
    else:
        rareness = "Unknown"

    damagetype = rd.choice(damagetypes)
    
    return {
        'Weapon Type': Manufacturer,
        'Weapon rarity': rareness,
        'damagetype on weapon': damagetype
    }
