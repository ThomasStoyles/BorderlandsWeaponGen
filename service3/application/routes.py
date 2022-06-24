from application import app
import random as rd

@app.route('/rarity', methods=['GET'])
def get_rarity():
    numbers = rd.randint(0,105)
    return str(numbers)

