
from models.repositories import ItemRepo
from schemas.schemas import ItemSchema
from flask import request
from db import db 
from sqlalchemy import select
from models.entities import Item
from flask import jsonify
from datetime import datetime

itemRepo = ItemRepo()
itemSchema = ItemSchema()
itemListSchema = ItemSchema(many=True)
ITEM_NOT_FOUND = "Item not found for id: {}"


def get(Id):
    item_data = itemRepo.fetchById(Id)
    if item_data:
        return itemSchema.dump(item_data)
    return {'message': ITEM_NOT_FOUND.format(Id)}, 404

def update(Id):
    item_data = itemRepo.fetchById(Id)
    item_req_json = request.get_json()
    item_req_json['Updated'] = datetime.now()
    if item_data:
        item_data.Name = item_req_json['Name']
        item_data.Checked = item_req_json['Checked']
        item_data.Type = item_req_json['Type']
        item_data.Age = item_req_json['Age']
        item_data.Description = item_req_json['Description']
        item_data.Date = datetime.strptime(item_req_json['Date'], '%Y-%M-%d')
        itemRepo.update(item_data)
        return itemSchema.dump(item_data)
    return {'message': ITEM_NOT_FOUND.format(Id)}, 404

def delete(Id):
    item_data = itemRepo.fetchById(Id)
    if item_data:
        itemRepo.delete(Id)
        return {'message': 'Item deleted successfully'}, 200
    return {'message': ITEM_NOT_FOUND.format(Id)}, 404

def create():
    item_req_json = request.get_json()
    item_data = itemSchema.load(item_req_json, session=db.session)
    itemRepo.create(item_data)
    return itemSchema.dump(item_data),201

def getAll():
    items = db.session.scalars(select(Item)).all()
    return jsonify(itemListSchema.dump(items)), 200