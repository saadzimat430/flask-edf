from db import db


class MarketRate(db.Model):
    __tablename__ = 'price'
    __table_args__ = {'schema': 'market-rates'}

    dates = db.Column(db.String(80), primary_key=True)
    be = db.Column(db.Float(precision=2))
    ch = db.Column(db.Float(precision=2))
    cz = db.Column(db.Float(precision=2))
    de_at = db.Column(db.Float(precision=2))
    dk1 = db.Column(db.Float(precision=2))
    dk2 = db.Column(db.Float(precision=2))
    es = db.Column(db.Float(precision=2))
    fr = db.Column(db.Float(precision=2))
    nl = db.Column(db.Float(precision=2))

    def __init__(self, dates, be, ch, cz, de_at, dk1, dk2, es, fr, nl):
        self.dates = dates
        self.be = be
        self.ch = ch
        self.cz = cz
        self.de_at = de_at
        self.dk1 = dk1
        self.dk2 = dk2
        self.es = es
        self.fr = fr
        self.nl = nl

    def json(self):
        return {'dates': self.dates,
                'be': self.be,
                'ch': self.ch,
                'cz': self.cz,
                'de_at': self.de_at,
                'dk1': self.dk1,
                'dk2': self.dk2,
                'es': self.es,
                'fr': self.fr,
                'nl': self.nl}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
