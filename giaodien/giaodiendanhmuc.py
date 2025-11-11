import tkinter as tk
from tkinter import ttk, messagebox

# Gọi các hàm đã tách trong module cammon
from cammon.insertdata import them_danhmuc
from cammon.delete_danhmuc import delete_danhmuc
from cammon.update_danhmuc import update_danhmuc
from cammon.get_danhmuc import get_all_danhmuc


# ====== HÀM HỖ TRỢ ======
def clear_form():
    """Xóa nội dung trong các ô nhập"""
    entry_ten.delete(0, tk.END)
    entry_mota.delete("1.0", tk.END)


def get_selected_id():
    """Lấy ID của dòng đang chọn trong bảng"""
    selected = tree.focus()
    if not selected:
        return None
    values = tree.item(selected, "values")
    if not values:
        return None
    try:
        return int(values[0])
    except Exception:
        return None


# ====== CÁC CHỨC NĂNG ======
def load_danhmuc():
    """Tải danh sách danh mục từ CSDL"""
    tree.delete(*tree.get_children())
    try:
        ds = get_all_danhmuc()
        for row in ds:
            tree.insert("", tk.END, values=row)
    except Exception as e:
        messagebox.showerror("Lỗi tải dữ liệu", f"{e}")


def them():
    """Thêm danh mục mới"""
    ten = entry_ten.get().strip()
    mota = entry_mota.get("1.0", tk.END).strip()
    if not ten:
        messagebox.showwarning("Cảnh báo", "Tên danh mục không được để trống!")
        return
    try:
        if them_danhmuc(ten, mota):
            messagebox.showinfo("Thành công", "Đã thêm danh mục mới!")
            clear_form()
            load_danhmuc()
        else:
            messagebox.showerror("Lỗi", "Không thể thêm danh mục!")
    except Exception as e:
        messagebox.showerror("Lỗi khi thêm", str(e))


def sua():
    """Sửa thông tin danh mục được chọn"""
    id_dm = get_selected_id()
    if id_dm is None:
        messagebox.showwarning("Cảnh báo", "Chọn danh mục cần sửa!")
        return

    ten_moi = entry_ten.get().strip()
    mota_moi = entry_mota.get("1.0", tk.END).strip()

    if not ten_moi:
        messagebox.showwarning("Cảnh báo", "Tên danh mục không được để trống!")
        return

    try:
        if update_danhmuc(id_dm, ten_moi, mota_moi):
            messagebox.showinfo("Thành công", "Đã cập nhật danh mục!")
            clear_form()
            load_danhmuc()
        else:
            messagebox.showerror("Lỗi", "Không thể cập nhật danh mục!")
    except Exception as e:
        messagebox.showerror("Lỗi khi sửa", str(e))


def xoa():
    """Xóa danh mục được chọn"""
    id_dm = get_selected_id()
    if id_dm is None:
        messagebox.showwarning("Cảnh báo", "Chọn danh mục cần xóa!")
        return

    if not messagebox.askyesno("Xác nhận", f"Bạn có chắc muốn xóa ID {id_dm}?"):
        return

    try:
        if delete_danhmuc(id_dm):
            messagebox.showinfo("Thành công", "Đã xóa danh mục!")
            clear_form()
            load_danhmuc()
        else:
            messagebox.showerror("Lỗi", "Không thể xóa danh mục (có thể đang được tham chiếu ở bảng khác).")
    except Exception as e:
        messagebox.showerror("Lỗi khi xóa", str(e))


def chon_danhmuc(event):
    """Khi chọn danh mục, hiển thị thông tin lên form"""
    selected = tree.focus()
    if not selected:
        return
    values = tree.item(selected, "values")
    if len(values) >= 3:
        entry_ten.delete(0, tk.END)
        entry_ten.insert(0, values[1])
        entry_mota.delete("1.0", tk.END)
        entry_mota.insert("1.0", values[2])


# ====== GIAO DIỆN CHÍNH ======
root = tk.Tk()
root.title("Quản lý danh mục - Tkinter + MySQL")
root.geometry("750x500")

# --- Form nhập ---
frame_top = tk.Frame(root)
frame_top.pack(pady=10)

tk.Label(frame_top, text="Tên danh mục:").grid(row=0, column=0, sticky="e")
entry_ten = tk.Entry(frame_top, width=40)
entry_ten.grid(row=0, column=1, padx=5)

tk.Label(frame_top, text="Mô tả:").grid(row=1, column=0, sticky="ne")
entry_mota = tk.Text(frame_top, width=40, height=4)
entry_mota.grid(row=1, column=1, padx=5, pady=5)

# --- Nút thao tác ---
frame_btn = tk.Frame(root)
frame_btn.pack(pady=5)

tk.Button(frame_btn, text="Thêm", width=10, command=them).grid(row=0, column=0, padx=5)
tk.Button(frame_btn, text="Sửa", width=10, command=sua).grid(row=0, column=1, padx=5)
tk.Button(frame_btn, text="Xóa", width=10, command=xoa).grid(row=0, column=2, padx=5)
tk.Button(frame_btn, text="Tải lại", width=10, command=load_danhmuc).grid(row=0, column=3, padx=5)

# --- Bảng danh mục ---
cols = ("ID", "Tên danh mục", "Mô tả")
tree = ttk.Treeview(root, columns=cols, show="headings", height=12)
for col in cols:
    tree.heading(col, text=col)
    tree.column(col, width=230)
tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# --- Gắn sự kiện chọn dòng ---
tree.bind("<<TreeviewSelect>>", chon_danhmuc)

# --- Hiển thị danh sách ban đầu ---
load_danhmuc()

root.mainloop()
