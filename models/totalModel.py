from db import db


class TotalModel(db.Model):
    __tablename__="total"

    id = db.Column(db.Integer, primary_key=True)
    total=db.Column(db.Integer) #visto da me

    def __init__(self, total):
        self.total=total

    @classmethod
    def find_by_id(cls):
        return TotalModel.query.filter_by(id=1).first()


    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()


def delete_slots_by_user_id(user_id):
    slots=FriendModel.query.filter_by(user_id=user_id)
    for i in slots:
        i.delete_from_db()
