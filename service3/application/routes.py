from application import app
from random import randint 


@app.route('/rarity', methods=['GET'])
def rarity():
    numbers = randint(0,105)
    return str(numbers)

