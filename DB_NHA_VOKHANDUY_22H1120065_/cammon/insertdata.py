from ketnoiDB.ketnoi_mysql import ket_noi_mysql
from mysql.connector import Error

def them_danhmuc(ten, mota):
    """Hàm thêm danh mục vào cơ sở dữ liệu"""
    conn = ket_noi_mysql()
    if conn is None:
        print("❌ Không thể kết nối MySQL")
        return False

    try:
        cursor = conn.cursor()
        sql = "INSERT INTO danhmuc (ten_danhmuc, mota) VALUES (%s, %s)"
        cursor.execute(sql, (ten, mota))
        conn.commit()
        print("✅ Đã thêm danh mục mới:", ten)
        return True
    except Error as e:
        print("❌ Lỗi khi thêm danh mục:", e)
        return False
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
