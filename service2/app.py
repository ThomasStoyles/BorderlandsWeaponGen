import flask as Flask
import random as rd 

app = Flask(__name__)

weapons = ['Sword','Bow','Axe','Staff','Trident', 'Hammer']

@app.route('/choose/weapon')
def choose_weapon():
    return rd.choice(weapons)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
