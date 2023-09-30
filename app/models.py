from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Hero(db.Model, SerializerMixin):
    __tablename__ = 'heros'

    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(100), nullable=False)
    super_name=db.Column(db.String(100), nullable=False)
    created_at =db.Column(db.DateTime, server_default=db.func.now())
    updated_at=db.Column(db.DateTime, onupdate=db.func.now())
    
    heropowers1 = db.relationship("HeroPower", backref="hero")
    
    
    # def to_dict(self):
    #     return {
    #         'id':self.id,
    #         "name" : self.name,
    #         "super_name" : self.super_name
            
    #     }
    
class Power(db.Model, SerializerMixin):   
    __tablename__ = "powers"
    
    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(100), nullable=False)
    description=db.Column(db.String(100), nullable=False)
    created_at =db.Column(db.DateTime, server_default=db.func.now())
    updated_at =db.Column(db.DateTime, onupdate=db.func.now())
    
    heropowers1 = db.relationship("HeroPower", backref="power")
    
    # def to_dict(self):
    #     return {
    #         'id':self.id,
    #         "name" : self.name,
    #         "description" : self.description
            
    #     }
    
class HeroPower(db.Model, SerializerMixin):
    __tablename__ = "heropowers" 
    
    id = db.Column(db.Integer, primary_key=True) 
    hero_id=db.Column(db.Integer(), db.ForeignKey("heros.id"), nullable=False )
    power_id=db.Column(db.Integer(), db.ForeignKey("powers.id"), nullable=False )
    strength = db.Column(db.String(50), nullable=False)
    created_at =db.Column(db.DateTime, server_default=db.func.now())
    updated_at =db.Column(db.DateTime, onupdate=db.func.now())
    
  
    # @validates("strength")
    # def validate_strength(self,key, strength):
    #     strengths = ["Strong", "Weak", "Average"]
        
    #     if strength not in strengths:
    #         raise ValueError("Provide valid strength")
    #     return strength
                
                
                
    # @validates('description') 
    # def validate_description(self,key, description):
    #     if len(description) < 20:
    #        raise ValueError("Dascription provided is too short")
    #     return description
    
    # def to_dict(self):
    #     return {
    #         'id':self.id,
    #         "strength" : self.strength
            
    #     }
        
            
      
    

# add any models you may need. 