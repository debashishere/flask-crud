from db import db
from datetime import datetime

class Item(db.Model):
    __tablename__ = "items"

    Id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(80), nullable=False)
    Checked = db.Column(db.Boolean, default=False, nullable=False)
    Type = db.Column(db.String(80), nullable=True)
    Age = db.Column(db.Integer, nullable=True)
    Description = db.Column(db.String(200), nullable=False, default='')
    Date = db.Column(db.Date, nullable=True)
    Created = db.Column(db.DateTime, nullable=False,
        default=datetime.utcnow)
    Updated = db.Column(db.DateTime, nullable=False,
        default=datetime.utcnow)

    def __repr__(self):
        return 'ItemModel(id=%d, Checked=%s, Name=%s, Type=%s, Age=%d, Description=%s, Date=%r)' % (
            self.Id, 
            self.Checked, 
            self.Name, 
            self.Type, 
            self.Age,
            self.Description,
            self.Date
            )

    def json(self):
        return {
            'Id':self.Id,
            'Checked': self.Checked,
            'Name': self.Name,
            'Type': self.Type,
            'Age': self.Age,
            'Descrption': self.Description,
            'Date': self.Date 
            }

