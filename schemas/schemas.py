
from ma import ma
from models.entities import Item
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from sqlalchemy.orm import relationship

class ItemSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Item
        include_relation = True
        load_instance = True
