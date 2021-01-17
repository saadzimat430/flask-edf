from flask import Flask, jsonify
from flask_restful import Api
from sqlalchemy.orm import Session

from resources.market_rate import MarketRateList
from db import db


app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost:5432/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)


@app.route('/')
def hello_world():
    return jsonify({"data": "test"})


api.add_resource(MarketRateList, '/market-rates')
db.init_app(app)


if __name__ == '__main__':
    app.run(debug=True)
