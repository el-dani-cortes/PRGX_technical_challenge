"""Module to init the application"""
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from extract.extraction import Extract
from models.engine import db, ma
from models.models import Data, DataSchema
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")

db.init_app(app)
ma.init_app(app)
with app.app_context():
    db.create_all()


@app.route('/extract', methods=['GET'])
def add_extraction():
    """Add extract information from path document to database"""
    pdf_path = request.args.get('doc_path')
    doc_data = Extract()
    try:
        image_path = doc_data.convert_PDF_to_image(pdf_path)
    except:
        return jsonify({"error_msg": "Couldn't find path to the pdf file"})
    image = doc_data.cv_image(image_path)
    text = doc_data.ocr_reading(image, image_path)
    data = doc_data.get_data_from_text(text)
    data['doc_path'] = pdf_path
    try:
        save_data = Data(
            vendor_name=data['Vendor name'],
            fiscal_number=data['Fiscal number'], contract=data['Contract number'],
            comments=data['Comments'],
            start_date=data['Start date'],
            end_date=data['End date'],
            doc_path=data['doc_path']
        )
        db.session.add(save_data)
        db.session.commit()
        result = [[True, save_data.id], data]
    except:
        return jsonify({"error_msg": "Couldn't store data in database"})
    return jsonify(result)


@app.route('/db_data/', methods=['GET'])
def get_extraction_data():
    """Query all data from database"""
    request_data = request.args.get('table_name')
    if request_data == 'EXTRACTION':
        data = Data.query.order_by(Data.id.desc()).all()
        data_schema = DataSchema(many=True)
        result = data_schema.dump(data)
        return jsonify(result)
    else:
        return jsonify({"error_msg": "Table name '{}\' doesn't exist".format(request_data)})


if __name__ == "__main__":
    app.run(debug=True)
