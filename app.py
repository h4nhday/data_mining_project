from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
import os
from datetime import datetime

app = Flask(__name__)

# Kết nối MongoDB
def connect_mongodb():
    try:
        client = MongoClient('mongodb://localhost:27017/')
        db = client['data_mining_project']
        return db
    except Exception as e:
        print(f"Lỗi kết nối MongoDB: {e}")
        return None

# Routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/users', methods=['GET'])
def get_users():
    db = connect_mongodb()
    if not db:
        return jsonify({"error": "Không thể kết nối database"}), 500
    
    users = list(db.users.find({}, {'_id': 0}))
    return jsonify(users)

@app.route('/api/products', methods=['GET'])
def get_products():
    db = connect_mongodb()
    if not db:
        return jsonify({"error": "Không thể kết nối database"}), 500
    
    products = list(db.products.find({}, {'_id': 0}))
    return jsonify(products)

@app.route('/api/invoices', methods=['GET'])
def get_invoices():
    db = connect_mongodb()
    if not db:
        return jsonify({"error": "Không thể kết nối database"}), 500
    
    invoices = list(db.invoices.find({}, {'_id': 0}))
    return jsonify(invoices)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000))) 