from sqlalchemy.orm import validates
from . import db
from sqlalchemy_serializer import SerializerMixin

class HeroPower(db.Model, SerializerMixin):
    __tablename__ = 'hero_powers'
    
    serialize_rules = ('-hero.hero_power', '-power.hero_power')
    
    id = db.Column(db.Integer, primary_key=True)
    hero_id = db.Column(db.Integer, db.ForeignKey('heroes.id'), nullable=False)
    power_id = db.Column(db.Integer, db.ForeignKey('powers.id'), nullable=False)
    strength = db.Column(db.String, nullable=False)
    
    hero = db.relationship('Hero', back_populates='hero_power')
    power = db.relationship('Power', back_populates='hero_power')
    
    @validates('strength')
    def validate_strength(self, key, strength):
        if strength not in ['Strong', 'Weak', 'Average']:
            raise ValueError("Strength must be 'Strong', 'Weak', or 'Average'")
        
        return strength