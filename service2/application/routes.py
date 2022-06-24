from application import app
import random as rd

Manufacturer = ['Atlas','Hyperion','Jakobs','Maliwan','Anshin', 'Vladof']

@app.route('/brand', methods=['GET'])
def brand():
    return rd.choice(brand)
