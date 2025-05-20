<<<<<<< HEAD
# Data Mining Project - Database Setup

Dự án này cung cấp các công cụ để thiết lập và quản lý cơ sở dữ liệu MongoDB cho dự án Data Mining.

## Tính năng

- Tạo collection users với schema cơ bản
- Upload dữ liệu từ file CSV và JSON lên MongoDB
- Quản lý kết nối database
- Hiển thị thông tin chi tiết về quá trình thực hiện

## Yêu cầu

- Python 3.x
- MongoDB
- Các thư viện Python:
  - pymongo
  - pandas
  - tqdm

## Cài đặt

1. Clone repository:
```bash
git clone [URL_REPOSITORY]
```

2. Cài đặt các thư viện cần thiết:
```bash
pip install -r requirements.txt
```

## Sử dụng

1. Đảm bảo MongoDB đang chạy trên máy local
2. Chạy script setup database:
```bash
python database_setup.py
```

## Cấu trúc dữ liệu

### Collection Users
- username (unique)
- email (unique)
- password
- full_name
- created_at
- last_login
- status
- role

### Collection Products
- Dữ liệu từ file Dataproducts.csv và Dataproducts.json

### Collection Invoices
- Dữ liệu từ file invoices_up.csv và invoices_up.json 
=======
# data_mining_project
>>>>>>> 83c11e3f93abca32751558185606acd85212875e
