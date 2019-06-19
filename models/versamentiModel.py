from db import db
import time

class VersamentiModel(db.Model):
    __tablename__="versamenti"

    id = db.Column(db.Integer, primary_key=True)
    giver=db.Column(db.Integer) #0 per matteo 1 per alessandra
    amount=db.Column(db.Integer)

    def __init__(self, giver, amount):
        self.giver = giver
        self.amount=amount


    @classmethod
    def find_by_id(cls, id):
        return VersamentiModel.query.filter_by(id=id).first()

    @classmethod
    def get_all(cls):
        a=[]
        for i in VersamentiModel.query.filter_by():
            a.append(i)
        return a

    @classmethod
    def find_by_giver(cls, giver):
        return VersamentiModel.query.filter_by(giver=giver).first()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
