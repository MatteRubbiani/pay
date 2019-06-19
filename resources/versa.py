from flask_restful import Resource, request
import time
from flask_jwt_extended import jwt_required, get_jwt_identity


from models.versamentiModel import VersamentiModel
from models.totalModel import TotalModel

class Versa(Resource):

    def post(self):
        id=int(request.args.get('id'))
        amount=int(request.args.get('amount'))
        versamentoModel=VersamentiModel(id, amount)
        versamentoModel.save_to_db()
        return "ok"

    def get(self):
        id=int(request.args.get('id'))
        total=0
        for i in VersamentiModel.get_all():
            if i.id==1:
                total=total-i.amount
            else:
                total=total+i.amount
        return total
