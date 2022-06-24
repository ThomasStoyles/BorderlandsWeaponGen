from flask import Flask
import random as rd 

app = Flask(__name__)

magics = {
    0: 'Fire'
    1: 'Grass'
    2: 'Water'
    3: 'Lightning'
    4: 'Ice'
    5: 'Psychic'
    6: 'Rock'
}
magic = rd.choice(list(magics.values()))

if weapons == 'Sword':
    var1 = 'Sword'
elif weapons == 'Axe':
    var1 = 'Axe'
elif weapons == 'Bow':
    var1 = 'Bow'
elif weapons == 'Staff':
    var1 = 'Staff'
elif weapons == 'Trident':
    var1 = 'Trident'
elif weapons == 'Hammer':
    var1 = 'Hammer'


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
