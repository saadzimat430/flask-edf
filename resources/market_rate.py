from flask_restful import Resource
from models.market_rate import MarketRate


class MarketRateList(Resource):

    def get(self):
        return {'market_rates': list(map(lambda rate: rate.json(), MarketRate.query.all()))}
