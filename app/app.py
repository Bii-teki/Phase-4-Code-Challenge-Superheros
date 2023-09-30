#!/usr/bin/env python3

from flask import Flask, make_response, jsonify, request
from flask_migrate import Migrate
from flask_restful import Api, Resource
# from flask_restx import Api, Resource, reqparse, fields
from flask_cors import CORS
import random


from models import db, Hero, HeroPower, Power

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///heropower.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

api = Api(app)

# patch_model = api.model('PowerPatch', {
#     'name': fields.String(description='Name of the power'),
#     'description': fields.String(description='Description of the power')
# })
# post_model = api.model('PostHeroPower', {
#     'strength': fields.String(strength='Strength')
# })

class Index(Resource):
    
    def get(self):
        response_dict = {
            "index": "Welcome to the Heros RESTful API",
        }
        return jsonify(response_dict)    

api.add_resource(Index, '/')



class HerosResource(Resource):
    def get(self):    
        return make_response(jsonify([hero.to_dict() for hero in Hero.query.all()]), 200)    

api.add_resource(HerosResource, "/heroes")


class HeroByIDResource(Resource):
    def get(self, id):
        heros = Hero.query.filter_by(id=id).filter()

        hero_list = []

        for hero in heros:
            powers = Power.query.join(HeroPower).filter(HeroPower.hero_id == hero.id).all()
            powers_dict = [power.to_dict() for power in powers]

            hero_dict = {
                "id": hero.id,
                "name": hero.name,
                "super_name": hero.super_name,
                "powers": powers_dict
            }
            hero_list.append(hero_dict)
            
        print('Fetched data:', hero_list)    

        return make_response(jsonify(hero_dict), 200)
    
    
api.add_resource(HeroByIDResource, "/heroes/<int:id>") 



# class PowersResource(Resource):
#     def get(self):    
#         return make_response(jsonify([power.to_dict() for power in Power.query.all()]), 200)    

# api.add_resource(PowersResource, "/powers")


# class PowerByIDResource(Resource):
#     def get(self, id):
#         return make_response(jsonify(Power.query.filter_by(id=id).first().to_dict()), 200)  
    
    
#     @api.doc(description='Update a power by ID')
#     @api.expect(patch_model)
#     @api.response(200, 'Power updated successfully')
#     @api.response(404, 'Power not found')
#     def patch(self, id):
#         data = request.json
#         record = Power.query.filter_by(id=id).first()

#         if record:
#             if 'name' in data:
#                 record.name = data['name']
#             if 'description' in data:
#                 record.description = data['description']

#             db.session.commit()
#             return make_response(jsonify(record.to_dict()), 200)
#         else:
#             return make_response(jsonify({"message": "Power not found"}), 404)

# api.add_resource(PowerByIDResource, "/powers/<int:id>")



# class HeroPowerResource(Resource):
#     @api.doc(description='creating new HeroPower')
#     @api.expect(post_model)
#     @api.response(200, 'Power updated successfully')
#     @api.response(404, 'Power not found')
    
#     def post(self):
#         data = request.get_json()
#         heros_id = [hero.id for hero in Hero.query.all() ]
#         powers_id = [power.id for power in Hero.query.all() ]
        
        
        
#         new_hero = HeroPower(
#             hero_id = random.choice(heros_id),
#             power_id =random.choice(powers_id),
#             strength = data["strength"]
#         )
        
#         db.session.add(new_hero)
#         db.session.commit()
        
#         return make_response(jsonify(new_hero.to_dict()), 200)
    
    
# api.add_resource(HeroPowerResource, "/hero_powers")    


 


# if __name__ == '__main__':
#     app.run(port=5000, debug=True)
