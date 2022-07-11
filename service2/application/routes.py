from application import app
import random as rd

Manufacturers = ['Atlas','Hyperion','Jakobs','Maliwan','Anshin', 'Vladof', 'a', 'b', 'c']

@app.route('/Manufacturer', methods=['GET'])
def Manufacturer():
    return rd.choice(Manufacturers)
