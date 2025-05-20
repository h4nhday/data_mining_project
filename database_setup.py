import pandas as pd
import json
from pymongo import MongoClient
import os
from tqdm import tqdm
import time
from datetime import datetime

def connect_mongodb():
    """Kết nối đến MongoDB và trả về client"""
    try:
        # Thử kết nối với MongoDB local
        connection_string = 'mongodb://localhost:27017/data_mining_project'
        client = MongoClient(connection_string, serverSelectionTimeoutMS=5000)
        
        # Kiểm tra kết nối
        client.admin.command('ping')
        print("✅ Kết nối MongoDB thành công!")
        return client
    except Exception as e:
        print(f"❌ Lỗi kết nối MongoDB: {e}")
        print("⚠️ Đang thử kết nối lại sau 5 giây...")
        time.sleep(5)
        return connect_mongodb()  # Thử kết nối lại

def create_user_collection(client):
    """Tạo collection users với schema cơ bản và dữ liệu mẫu"""
    try:
        db = client['data_mining_project']
        collection = db['users']
        
        # Xóa collection cũ nếu tồn tại
        if "users" in db.list_collection_names():
            collection.drop()
            print("🗑️ Đã xóa collection users cũ")
        
        # Tạo index cho email và username
        collection.create_index("email", unique=True)
        collection.create_index("username", unique=True)
        
        # Tạo dữ liệu mẫu
        sample_user = {
            "username": "test_user",
            "email": "test@example.com",
            "password": "hashed_password_here",
            "full_name": "Test User",
            "created_at": datetime.now(),
            "last_login": datetime.now(),
            "status": "active",
            "role": "user"
        }
        
        # Thêm dữ liệu mẫu vào collection
        collection.insert_one(sample_user)
        
        # Kiểm tra xem collection đã được tạo chưa
        if "users" in db.list_collection_names():
            print("✅ Đã tạo collection users thành công!")
            print(f"📊 Số lượng documents trong collection: {collection.count_documents({})}")
            
            # In ra dữ liệu mẫu để kiểm tra
            print("\n📋 Dữ liệu mẫu trong collection:")
            for user in collection.find():
                print(f"""
                Username: {user['username']}
                Email: {user['email']}
                Full Name: {user['full_name']}
                Role: {user['role']}
                Status: {user['status']}
                Created At: {user['created_at']}
                Last Login: {user['last_login']}
                """)
        else:
            print("❌ Không thể tạo collection users")
            
    except Exception as e:
        print(f"❌ Lỗi khi tạo collection users: {e}")

def upload_csv(client, file_path, collection_name):
    """Upload file CSV lên MongoDB"""
    try:
        print(f"\n📁 Đang xử lý file {file_path}...")
        start_time = time.time()
        
        # Đọc file CSV
        df = pd.read_csv(file_path)
        print(f"✅ Đã đọc xong file {file_path}")
        print(f"📊 Số lượng records: {len(df)}")
        
        # Chuyển DataFrame thành list of dictionaries
        data = df.to_dict('records')
        
        # Chọn database và collection
        db = client['data_mining_project']
        collection = db[collection_name]
        
        # Xóa collection cũ nếu tồn tại
        if collection_name in db.list_collection_names():
            collection.drop()
            print(f"🗑️ Đã xóa collection {collection_name} cũ")
        
        # Upload lên MongoDB với thanh tiến trình
        print(f"⏳ Đang upload lên collection {collection_name}...")
        chunk_size = 1000
        total_chunks = (len(data) + chunk_size - 1) // chunk_size
        
        for i in tqdm(range(0, len(data), chunk_size), total=total_chunks):
            chunk = data[i:i + chunk_size]
            if chunk:
                collection.insert_many(chunk)
        
        end_time = time.time()
        duration = end_time - start_time
        
        print(f"✅ Đã upload xong {collection_name}")
        print(f"📊 Số lượng records trong collection: {collection.count_documents({})}")
        print(f"⏱️ Thời gian thực hiện: {duration:.2f} giây")
        
    except Exception as e:
        print(f"❌ Lỗi khi xử lý file {file_path}: {e}")

def upload_json(client, file_path, collection_name):
    """Upload file JSON lên MongoDB"""
    try:
        print(f"\n📁 Đang xử lý file {file_path}...")
        start_time = time.time()
        
        # Đọc file JSON
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        print(f"✅ Đã đọc xong file {file_path}")
        print(f"📊 Số lượng records: {len(data)}")
        
        # Chọn database và collection
        db = client['data_mining_project']
        collection = db[collection_name]
        
        # Xóa collection cũ nếu tồn tại
        if collection_name in db.list_collection_names():
            collection.drop()
            print(f"🗑️ Đã xóa collection {collection_name} cũ")
        
        # Upload lên MongoDB với thanh tiến trình
        print(f"⏳ Đang upload lên collection {collection_name}...")
        chunk_size = 1000
        total_chunks = (len(data) + chunk_size - 1) // chunk_size
        
        for i in tqdm(range(0, len(data), chunk_size), total=total_chunks):
            chunk = data[i:i + chunk_size]
            if chunk:
                collection.insert_many(chunk)
        
        end_time = time.time()
        duration = end_time - start_time
        
        print(f"✅ Đã upload xong {collection_name}")
        print(f"📊 Số lượng records trong collection: {collection.count_documents({})}")
        print(f"⏱️ Thời gian thực hiện: {duration:.2f} giây")
        
    except Exception as e:
        print(f"❌ Lỗi khi xử lý file {file_path}: {e}")

def main():
    """Hàm chính để thực hiện setup database"""
    print("🚀 Bắt đầu quá trình setup database...")
    
    # Kết nối MongoDB
    client = connect_mongodb()
    if not client:
        return
    
    try:
        # Tạo collection users
        create_user_collection(client)
        
        # Upload các file dữ liệu
        upload_csv(client, 'Dataproducts.csv', 'products')
        upload_json(client, 'Dataproducts.json', 'products_json')
        upload_csv(client, 'invoices_up.csv', 'invoices')
        upload_json(client, 'invoices_up.json', 'invoices_json')
        
        # In ra danh sách collections
        print("\n📋 Danh sách collections trong database:")
        db = client['data_mining_project']
        for collection in db.list_collection_names():
            count = db[collection].count_documents({})
            print(f"- {collection}: {count} records")
            
    except Exception as e:
        print(f"❌ Lỗi trong quá trình xử lý: {e}")
    finally:
        client.close()
        print("\n👋 Đã đóng kết nối MongoDB")

if __name__ == "__main__":
    main() 