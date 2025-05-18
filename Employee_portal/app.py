from flask import Flask, request, jsonify
import pandas as pd

from database.db import SessionLocal
from database.setup_utils import create_all_tables
from utils.excel_loader import insert_data_from_excel
from database.procedures import * 
from utils.utils import *
from flask import Flask
from flask_cors import CORS


app = Flask(__name__)
CORS(app)  # This will allow all domains by default

create_all_tables()  # Create tables at startup

# 📤 Upload Excel Data Route
@app.route('/upload/<table_name>', methods=['POST'])
def upload_excel(table_name):
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    if not file.filename.endswith(('.xlsx', '.xls')):
        return jsonify({"error": "Only Excel files are allowed."}), 400

    try:
        df = pd.read_excel(file)
        db = SessionLocal()
        insert_data_from_excel(table_name, df, db)
        db.close()
        return jsonify({"status": "Success", "table": table_name}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# 📥 Fetch Employee Data (from stored procedure)
@app.route('/data/employee_data', methods=['GET'])
def get_employee_data():
    db = SessionLocal()
    try:
        data = fetch_all_employee_data(db)
        return jsonify(data), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        db.close()

@app.route('/data/employee_rating', methods=['GET'])
def get_employee_rating():
    db = SessionLocal()
    try:
        data = fetch_all_employee_rating(db)
        return jsonify(data), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        db.close()


@app.route('/data/industry_compensation', methods=['GET'])
def get_employee_industry_compensation():
    db = SessionLocal()
    try:
        data = fetch_all_industry_compensation(db)
        return jsonify(data), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        db.close()


@app.route('/data/filtered_employees', methods=['GET'])
def get_filtered_employees():
    role = request.args.get('role')
    include_inactive = request.args.get('include_inactive', 'false').lower() == 'true'
    location = request.args.get('location')

    db = SessionLocal()
    try:
        data = fetch_filtered_employee_data(db, role, include_inactive, location)
        return jsonify(data), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        db.close()

@app.route('/data/experience_distribution', methods=['GET'])
def get_experience_distribution():
    location = request.args.get('location')
    role = request.args.get('role')

    db = SessionLocal()
    try:
        data = fetch_experience_distribution(db, location, role)
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        db.close()


@app.route('/download/employee_data', methods=['GET'])
def download_employee_data():
    location = request.args.get('location')
    role = request.args.get('role')
    min_exp = request.args.get('min_exp')
    max_exp = request.args.get('max_exp')

    db = SessionLocal()
    try:
        csv_data = generate_filtered_csv(db, location, role, min_exp, max_exp)
        return Response(
            csv_data.getvalue(),
            mimetype='text/csv',
            headers={"Content-Disposition": "attachment;filename=filtered_employee_data.csv"}
        )
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        db.close()


if __name__ == '__main__':
    app.run(debug=True)
