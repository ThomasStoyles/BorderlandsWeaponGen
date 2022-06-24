from application import app
import random as rd

Manufacturers = ['Atlas','Hyperion','Jakobs','Maliwan','Anshin', 'Vladof']

@app.route('/Manufacturer', methods=['GET'])
def Manufacturer():
    return rd.choice(Manufacturers)
