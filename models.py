from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Flight(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    type = db.Column(db.String(15), nullable=False)  # "Nacional" o "Internacional"
    price = db.Column(db.Float, nullable=False)
    
    def __init__(self, name, type, price):
        self.name = name
        self.type = type
        self.price = price

