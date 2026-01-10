"""
- Xây dựng : Lớp đối tượng ->  Lớp quản lý (nhập vào, in ra) ->  hàm main
- Sau khi xây dựng đọc ghi file: thêm hàm xuất file để cập nhật dữ liệu trong file
- OOP, collection, unpacking, xử lý lỗi, string
"""
import os.path
from datetime import datetime

# Hàm format ns về dạng dd/mm/yyyy 1/1/2003 -> 01/01/2003
def format_dob(ns):
    d, m, y = ns.strip().split("/")  # d = 1, m = 1, y = 2003, unpacking
    if len(d) == 1:
        d = "0" + d  # d = 01
    if len(m) == 1:
        m = "0" + m  # m = 01
    return f"{d}/{m}/{y}"  # d + "/" + m + "/" + y

# Nhập điểm (đảm bảo từ 0-10)
def nhap_diem(label):
    while True:
        try:
            diem = float(input(f"Nhập vào điểm {label}: "))
            if 0 <= diem <= 10:
                return diem
            else:
                # Báo lỗi khi giá trị vượt ngoài tầm
                print(">>> Lỗi: Vui lòng nhập điểm từ 0 đến 10.")
        except ValueError: # giá trị khác số
            print(">>> Lỗi: Vui lòng nhập điểm từ 0 đến 10.")

# Nhập ngày sinh
def nhap_ns():
    while True:
        try:
            inp_dob = input("Nhập vào ngày sinh (dd/mm/yyyy): ")
            dob = datetime.strptime(inp_dob, "%d/%m/%Y").date()
            return format_dob(inp_dob)
        except ValueError:
            print(">>> Lỗi: Vui lòng nhập ngày hợp lệ.")

class SinhVien:
    def __init__(self, msv, ten, gt, ns, toan, ly, hoa):
        self.msv = msv
        self.ten = ten
        self.gt = gt
        self.ns = ns
        self.toan = toan
        self.ly = ly
        self.hoa = hoa
        self.dtb = self.tinh_dtb()
        self.xl = self.xeploai()

    def tinh_dtb(self):
        avg = (self.toan + self.ly + self.hoa) / 3  # làm tròn 2 số sau dấu phẩy
        return round(avg, 2)

    def xeploai(self):
        avg = self.dtb
        if avg >= 8:
            return "Giỏi"
        elif avg >= 6.5:
            return "Khá"
        elif avg >= 5:
            return "Trung Bình"
        else:
            return "Yếu"

    def __str__(self):
        return f"{self.msv}|{self.ten}|{self.gt}|{self.ns}|{self.toan}|{self.ly}|{self.hoa}|{self.dtb}|{self.xl}"

# Xây dựng class Quản lý
class QuanLy:
    def __init__(self):
        self.students = []  # list chứa danh sách SinhVien

    # Kiểm tra mã sinh viên (msv) đã tồn tại chưa
    def check(self, msv):
        for st in self.students:
            if st.msv == msv:
                return True
        return False

    def nhap_sv(self):
        msv = input("Nhập vào mã sinh viên: ")
        if self.check(msv):
            print("Mã sinh viên đã tồn tại")
            return None
        else:
            ten = input("Nhập vào tên sinh viên: ")
            # gt = nhap_gt(input("Nhập vào giới tính (1: Nam/0: Nu): "))
            gt = input("Nhập vào giới tính (Nam/Nu): ")
            ns = nhap_ns()
            toan = nhap_diem("Toán")
            ly = nhap_diem("Lý")
            hoa = nhap_diem("Hóa")
            return SinhVien(msv, ten, gt, ns, toan, ly, hoa)

    def in_ds(self):
        if len(self.students) == 0:
            print("Chưa có sinh viên nào trong danh sách.")
        else:
            print("Danh sách sinh viên:")
            for st in self.students:
                print(st)

    def them_sv(self, sv):
        if sv is None:
            return
        self.students.append(sv)
        self.xuat_file()
        print(f"Thêm sinh viên {sv.ten} thành công")

    def xoa_sv(self, msv):
        if not self.check(msv):
            print(f"Mã sinh viên {msv} không tồn tại")
        else:
            for st in self.students:
                if st.msv == msv:
                    self.students.remove(st)
            self.xuat_file()
            print(f"Xóa sinh viên {msv} thành công")

    def sua_sv(self, msv):
        if not self.check(msv):
            print(f"Mã sinh viên {msv} không tồn tại")
        else:
            ten = input("Nhập vào tên sinh viên: ")
            gt = input("Nhập vào giới tính (Nam/Nu)")
            ns = input("Nhập vào ngày sinh: ")
            toan = input("Nhập vào điểm Toán: ")
            ly = input("Nhập vào điểm Lý: ")
            hoa = input("Nhập vào điểm Hóa: ")
            new_sv = SinhVien(
                msv, ten, gt, ns.capitalize(), float(toan), float(ly), float(hoa)
            )
            for i, st in enumerate(self.students):
                if st.msv == msv:
                    self.students[i] = new_sv
            print(f"Cập nhật thông tin sinh viên {msv} thành công")

    def sua_sv2(self, msv):
        cur_sv = None
        for i, st in enumerate(self.students):
            if st.msv == msv:
                cur_sv = self.students[i]
                break
        if cur_sv == None:
            print(f"Mã sinh viên {msv} không tồn tại")
            return

        while True:
            print("Chọn thông tin sinh viên cần chỉnh sửa:")
            print("1. Tên")
            print("2. Giới tính")
            print("3. Ngày sinh")
            print("4. Điểm Toán")
            print("5. Điểm Lý")
            print("6. Điểm Hóa")
            print("0. Thoát")
            try:
                act = int(input("Chọn trường cần sửa: "))
                if act > 6 or act < 0:
                    print("Vui lòng chọn hành động hợp lệ.")
                if act == 1:
                    cur_sv.ten = input("Nhập vào tên sinh viên: ")
                elif act == 2:
                    cur_sv.gt = input("Nhập vào giới tính (Nam/Nu): ")
                elif act == 3:
                    cur_sv.ns = nhap_ns()
                elif act == 4:
                    cur_sv.toan = nhap_diem("Toán")
                elif act == 5:
                    cur_sv.ly = nhap_diem("Lý")
                elif act == 6:
                    cur_sv.hoa = nhap_diem("Hóa")
                elif act == 0:
                    cur_sv.dtb = cur_sv.tinh_dtb()
                    cur_sv.xl = cur_sv.xeploai()
                    self.xuat_file()
                    print("Cập nhật thành công.")
                    break
            except Exception as e:
                print(e)



    def tk_sv(self, opt, keyword):
        res = []
        if opt == 1:
            for st in self.students:
                # gõ đúng mã sinh viên
                if keyword.lower() == st.msv.lower():
                    res.append(st)
        else:
            for st in self.students:
                # gõ không cần đầy đủ chỉ cần chưa tên
                if keyword.lower() in st.ten.lower():
                    res.append(st)
        if len(res) == 0:
            print("Không có kết quả")
        else:
            for st in res:
                print(st)

    def sx_sv(self, opt):
        res = []
        option = "tên" if opt == 1 else "điểm trung bình giảm dần"
        if opt == 1:
            # Sắp xếp theo tên (alphabet)
            res = sorted(self.students, key=lambda st: st.ten)
        else:
            # res = sorted(self.students, key=lambda st: -st.dtb)
            res = sorted(self.students, key=lambda st: st.dtb, reverse=True)
        print(f"Danh sách sinh viên sắp xếp theo {option} :")
        for st in res:
            print(st)

    def thongke(self):
        res = {"Giỏi": 0, "Khá": 0, "Trung Bình": 0, "Yếu": 0}
        for st in self.students:
            res[st.xl] = res.get(st.xl, 0) + 1
        print("Bảng thống kê học lực sinh viên: ")
        for k, v in res.items(): # [("Giỏi", 2), (), ()]
            print(f"{k}: {v} sinh viên")

    def xuat_file(self):
        with open("tests.txt", "w", encoding="utf-8") as f:
            for st in self.students:
                f.write(f"{st}\n")
        print(">>> Đã lưu danh sách vào file: tests.txt")

    def doc_file(self):
        self.students.clear()
        with open("tests.txt", "r", encoding="utf-8") as f:
            for line in f:
                tmp = line.strip().split("|") # [SV001, Ngyen...]
                # Nếu dữ liệu không đẩy đủ -> bỏ qua
                if len(tmp) < 9:
                    continue
                msv, ten, gt, ns, toan, ly, hoa, dtb, xl = tmp
                sv = SinhVien(msv, ten, gt, ns, float(toan), float(ly), float(hoa))
                sv.dtb = float(dtb)
                sv.xl = xl
                self.students.append(sv)

# Hàm main
if __name__ == "__main__":
    ql = QuanLy()  # Khai báo lớp Quản lý
    action = -1  # Biến lưu trữ hành động

    # Vòng lặp chương trình -> Chương trình chạy liên tục đến khi chọn 0 để thoát
    while True:
        print("\n=======QUẢN LÝ SINH VIÊN========")
        print("1. Thêm sinh viên")
        print("2. Hiển thị danh sách")
        print("3. Cập nhật thông tin")
        print("4. Xóa sinh viên")
        print("5. Tìm kiếm sinh viên")
        print("6. Sắp xếp sinh viên")
        print("7. Thống kê xếp loại sinh viên")
        print("8. Xuất file ")
        print("9. Tải dữ liệu từ file")
        print("0. Thoát")
        print("================================\n")

        try:
            action = int(input("Chọn chức năng: "))
            if action > 9 or action < 0:
                print("Vui lòng chọn chức năng hợp lệ")
                continue
            # Kiểm tra nếu file tồn tại thì tải dữ liệu lên
            if os.path.exists("tests.txt"):
                ql.doc_file()

            if action == 0:
                print("Thoát chương trình.")
                break  # thoát khỏi vòng lặp while True
            elif action == 1:
                st = ql.nhap_sv()
                ql.them_sv(st)
            elif action == 2:
                ql.in_ds()
            elif action == 3:
                msv = input("Nhập mã sinh viên cần sửa: ")
                ql.sua_sv2(msv)
            elif action == 4:
                msv = input("Nhập mã sinh viên cần xóa: ")
                ql.xoa_sv(msv)
            elif action == 5:
                while True:
                    print("Tiêu chí tìm kiếm: ")
                    print("1. Mã sinh viên")
                    print("2. Tên sinh viên")
                    act = int(input("Chọn tiêu chí: "))
                    if act < 1 or act > 2:
                        print("Vui lòng chọn giá trị hợp lệ")
                        continue
                    keyword = input("Nhập từ khóa: ")
                    ql.tk_sv(act, keyword)
                    break
            elif action == 6:
                while True:
                    print("Tiêu chí sắp xếp: ")
                    print("1. Tên sinh viên")
                    print("2. Điểm trung bình giảm dần")
                    act = int(input("Chọn tiêu chí: "))
                    if act < 1 or act > 2:
                        print("Vui lòng chọn giá trị hợp lệ")
                        continue
                    ql.sx_sv(act)
                    break
            elif action == 7:
                ql.thongke()
            elif action == 8:
                ql.xuat_file()
            elif action == 9:
                ql.doc_file()
                print(">>> Đã tải dữ liệu thành công từ file.")
                ql.in_ds()
        except Exception as e:
            print(e)
