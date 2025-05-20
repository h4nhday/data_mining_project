<<<<<<< HEAD
from pymongo import MongoClient
from datetime import datetime

def create_user_collection():
    """Tạo collection users với schema cơ bản và dữ liệu mẫu"""
    try:
        # Kết nối MongoDB
        client = MongoClient('mongodb://localhost:27017/')
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
    finally:
        client.close()
        print("\n👋 Đã đóng kết nối MongoDB")

if __name__ == "__main__":
=======
from pymongo import MongoClient
from datetime import datetime

def create_user_collection():
    """Tạo collection users với schema cơ bản và dữ liệu mẫu"""
    try:
        # Kết nối MongoDB
        client = MongoClient('mongodb://localhost:27017/')
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
    finally:
        client.close()
        print("\n👋 Đã đóng kết nối MongoDB")

if __name__ == "__main__":
>>>>>>> 83c11e3f93abca32751558185606acd85212875e
    create_user_collection()*