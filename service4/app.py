from flask import Flask
import random as rd 

app = Flask(__name__)

damagetypes = {
    0: 'Normal'
    1: 'Fire'
    2: 'Electric'
    3: 'Ice'
    4: 'Corrosive'
    5: 'Sluge'
    6: 'Explosive'
}

damagetypes = rd.choice(list(damagetypes.values()))

if Manufacturer == 'Atlas':
    var1 = 'Atlas'
elif Manufacturer == 'Hyperion':
    var1 = 'Hyperion'
elif Manufacturer == 'Jakobs':
    var1 = 'Jakobs'
elif Manufacturer == 'Maliwan':
    var1 = 'Maliwan'
elif Manufacturer == 'Anshin':
    var1 = 'Anshin'
elif Manufacturer == 'Vladof':
    var1 = 'Vladof'


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

final_weapon = {
    'Weapon Type': var1,
    'Weapon rarity': rareness,
    'Magic on weapon': magic
    
}


if __name__ == '__main__':
    app.run(host='0.0.0.0')
