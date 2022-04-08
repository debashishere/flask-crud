from db import db
from models.entities import Item
from typing import List


class ItemRepo:
    
 def create(self,item):
    db.session.add(item)
    db.session.commit()
    
 def fetchById(self,_Id)-> 'Item':
     return db.session.query(Item).filter_by(Id=_Id).first()
 
 def fetchAll(self) -> List['Item']:
     return db.session.query(Item).all()
 
 def delete(self,_Id) -> None:
     item= db.session.query(Item).filter_by(Id=_Id).first()
     db.session.delete(item)
     db.session.commit()
     
 def update(self,item_data):
    db.session.merge(item_data)
    db.session.commit()