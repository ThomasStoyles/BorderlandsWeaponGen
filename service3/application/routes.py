from application import app
import random as rd 

rarities = ["Common", "Uncommon", "Rare", "Epic", "Legendary", "Unknown", "Pearlescent"]

@app.route('/rarity', methods=['GET'])
def rarity():
    return rd.choice(rarities)
    
