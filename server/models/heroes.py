from . import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy 

class Hero(db.Model, SerializerMixin):
    __tablename__ = 'heroes'
    
    serialize_rules= ('-hero_power.hero',)
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    super_name = db.Column(db.String, nullable=False)
    
    hero_power = db.relationship('HeroPower', back_populates='hero', cascade="all, delete-orphan")