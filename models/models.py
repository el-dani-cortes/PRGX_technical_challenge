"""Module to create models and schemas"""
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from models.engine import db, ma


class Data(db.Model):
    """Model of the table for database"""
    __tablename__ = 'EXTRACTION'
    id = db.Column(db.Integer, primary_key=True)
    vendor_name = db.Column(db.String(100), nullable=False)
    fiscal_number = db.Column(db.String(50), nullable=False)
    contract = db.Column(db.String(50), nullable=False)
    start_date = db.Column(db.String(20), nullable=False)
    end_date = db.Column(db.String(20), nullable=False)
    comments = db.Column(db.String(500))
    doc_path = db.Column(db.String(100), nullable=False)


class DataSchema(ma.SQLAlchemyAutoSchema):
    """Model to serialize data"""
    class Meta:
        """Meta class"""
        model = Data
