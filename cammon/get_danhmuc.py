from mysql.connector import Error
from ketnoiDB.ketnoi_mysql import ket_noi_mysql  # import hàm kết nối MySQL

def get_all_danhmuc():
    """Hàm lấy danh sách tất cả danh mục từ bảng danhmuc"""
    conn = ket_noi_mysql()
    if conn is None:
        print("❌ Không thể kết nối cơ sở dữ liệu.")
        return []

    try:
        cursor = conn.cursor()
        sql = "SELECT id, ten_danhmuc, mota FROM danhmuc ORDER BY id ASC"
        cursor.execute(sql)
        records = cursor.fetchall()

        if records:
            print("📋 Danh sách danh mục:")
            for row in records:
                print(f"ID: {row[0]} | Tên: {row[1]} | Mô tả: {row[2]}")
        else:
            print("⚠️ Chưa có danh mục nào trong cơ sở dữ liệu.")

        return records

    except Error as e:
        print("❌ Lỗi khi lấy danh sách danh mục:", e)
        return []

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
