from flask import Flask 
import random as rd 

app = Flask(__name__)

@app.route(/get/rarity)
def get_rarity():
    return rd.randint(0,105)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
