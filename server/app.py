from flask import Flask, request, make_response, jsonify
from models import db, Hero, Power, HeroPower
from flask_migrate import Migrate
from flask_cors import CORS
from flask_restx import Api, Resource

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///superheroes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

api = Api(app)
CORS(app)
migrate = Migrate(app, db)

db.init_app(app)

@api.route('/')
class index(Resource):
    def get(self):
        return make_response({"message": "Welcome to the Superheroes API"}, 200, {'Content-Type': 'application/json'})

@api.route('/heroes', methods=['GET'])
class Heroes(Resource):
    def get(self):
        heroes = [x.to_dict(rules=('-hero_power',)) for x in Hero.query.all()]
        return make_response(heroes, 200, {'Content-Type': 'application/json'})


@api.route('/heroes/<int:id>', methods=['GET'])
class HeroByID(Resource):
    def get(self, id):
        hero = Hero.query.filter_by(id=id).first()
        
        if not hero:
            res = {'error': 'Hero not found'}
            code = 404
        else:
            res = hero.to_dict(rules=('-hero_power',))
            code = 200
            
        return make_response(res, code, {'Content-Type': 'application/json'})


@api.route('/powers', methods=['GET'])
class Powers(Resource):
    def get(self):
        powers = [x.to_dict(rules=('-hero_power',)) for x in Power.query.all()]
        return make_response(powers, 200, {'Content-Type': 'application/json'})


@api.route('/powers/<int:id>', methods=['GET', 'PATCH'])
class PowerByID(Resource):
    def get(self, id):
        power = Power.query.filter_by(id=id).first()
        
        if not power:
            res = {'error': 'Power not found'}
            code = 404
        else:
            res = power.to_dict(rules=('-hero_power',))
            code = 200
            
        return make_response(res, code, {'Content-Type': 'application/json'})
    
    def patch(self, id):
        power = Power.query.filter_by(id=id).first()
        
        if not power:
            res = {'error': 'Power not found'}
            code = 404
        else:
            try:
                json = request.get_json()
                for attr in json:
                    setattr(power, attr, json[attr])
                db.session.commit()
                res = {"description": "Valid Updated Description"}
                code = 200
                
            except Exception as e:
                res = {'errors': ["validation errors"]}
                code = 400
                
        return make_response(res, code, {'Content-Type': 'application/json'})

@api.route('/hero_powers', methods=['POST'])
class HeroPowers(Resource):
    def post(self):
        try:
            json = request.get_json()
            hero_power = HeroPower(strength=json['strength'], hero_id=json['hero_id'], power_id=json['power_id'])
            
            db.session.add(hero_power)
            db.session.commit()
            
            res = hero_power.to_dict()
            code = 201
            
        except Exception as e:
            res = {'errors': ["validation errors"]}
            code = 400
            
        return make_response(res, code, {'Content-Type': 'application/json'})

if __name__ == "__main__":
    app.run(debug=True, port=5555)