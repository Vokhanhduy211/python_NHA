import mysql.connector
from mysql.connector import Error

def ket_noi_mysql():
    """Hàm kết nối đến MySQL (port 3307) và trả về đối tượng connection"""
    try:
        connection = mysql.connector.connect(
            host='localhost',        # Địa chỉ máy chủ
            port=3307,               # ⚡ Cổng MySQL (thay vì 3306)
            user='root',             # Tên người dùng MySQL
            password='',             # Mật khẩu (nếu có)
            database='qlthuocankhang'       # Tên database
        )

        if connection.is_connected():
            print("✅ Kết nối MySQL (port 3307) thành công!")
            return connection

    except Error as e:
        print("❌ Lỗi khi kết nối MySQL:", e)
        return None
