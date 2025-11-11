from mysql.connector import Error
from ketnoiDB.ketnoi_mysql import ket_noi_mysql

def delete_danhmuc(id_danhmuc):
    """Xóa danh mục theo ID"""
    conn = ket_noi_mysql()
    if conn is None:
        print("❌ Không thể kết nối CSDL.")
        return False

    try:
        cursor = conn.cursor()
        sql = "DELETE FROM danhmuc WHERE id = %s"
        cursor.execute(sql, (id_danhmuc,))
        conn.commit()

        if cursor.rowcount > 0:
            print(f"✅ Đã xóa danh mục ID = {id_danhmuc}")
            return True
        else:
            print(f"⚠️ Không tìm thấy danh mục ID = {id_danhmuc}")
            return False

    except Error as e:
        # Nếu bị lỗi khóa ngoại (MySQL Error Code 1451)
        if e.errno == 1451:
            print(f"⚠️ Không thể xóa danh mục ID {id_danhmuc}: đang được tham chiếu ở bảng khác.")
            return False
        print("❌ Lỗi khi xóa danh mục:", e)
        return False

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
