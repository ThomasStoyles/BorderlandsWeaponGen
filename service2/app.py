import flask as Flask
import random as rd 

app = Flask(__name__)

Manufacturer = ['Atlas','Hyperion','Jakobs','Maliwan','Anshin', 'Vladof']

@app.route('/choose/brand')
def choose_brand():
    return rd.choice(brand)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
