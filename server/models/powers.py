from . import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy

class Power(db.Model, SerializerMixin):
    __tablename__ = 'powers'
    
    serialize_rules = ('-hero_power.power',)
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String(20), nullable=False)
    
    hero_power = db.relationship('HeroPower', back_populates='power', cascade="all, delete-orphan")