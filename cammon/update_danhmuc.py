from mysql.connector import Error
from ketnoiDB.ketnoi_mysql import ket_noi_mysql


def update_danhmuc(id_danhmuc, ten_danhmuc, mota):
    """Cập nhật danh mục theo ID"""
    conn = ket_noi_mysql()
    if conn is None:
        print("❌ Không thể kết nối cơ sở dữ liệu.")
        return False

    try:
        cursor = conn.cursor()
        sql = "UPDATE danhmuc SET ten_danhmuc = %s, mota = %s WHERE id = %s"
        cursor.execute(sql, (ten_danhmuc, mota, id_danhmuc))
        conn.commit()

        if cursor.rowcount > 0:
            print(f"✅ Cập nhật danh mục ID {id_danhmuc} thành công.")
            return True
        else:
            print(f"⚠️ Không tìm thấy danh mục có ID {id_danhmuc}.")
            return False

    except Error as e:
        print("❌ Lỗi khi cập nhật danh mục:", e)
        return False

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
