from datetime import datetime
from os import path
import csv

class SinhVien:
    def __init__(self, msv, ten, gt, ns, toan, li, hoa):
        self.msv = msv
        self.ten = ten
        self.gt = gt
        self.ns = ns
        self.toan = toan
        self.li = li
        self.hoa = hoa
        self.dtb = self.tinh_dtb()
        self.xl = self.xeploai()
    
    def tinh_dtb(self):
        diem = (self.toan + self.li + self.hoa) / 3
        return round(diem, 2)

    def xeploai(self):
        diem = self.dtb
        if diem >= 8:
            return "Giỏi"
        elif diem >= 6.5:
            return "Khá"
        elif diem >= 5:
            return "Trung bình"
        else:
            return "Yếu"
    
    def __str__(self): 
        return f"{self.msv}|{self.ten}|{self.gt}|{self.ns}|{self.toan}|{self.li}|{self.hoa}|{self.dtb}|{self.xl}"

def nhap_gt():
    while True:
        try:
            opt = int(input("Chọn giới tính (Nữ: 0/ Nam: 1): "))
            if opt == 0:
                return "Nữ"
            elif opt == 1:
                return "Nam"
            else:
                print(">>> Vui lòng nhập giá trị hợp lệ.")
        except Exception:
            print(">>> Vui lòng nhập giá trị hợp lệ.")

def format_date(ns):
    d, m, y = ns.split("/")
    if len(d) == 1 : d = "0" + d
    if len(m) == 1 : m = "0" + m
    return f"{d}/{m}/{y}"

def nhap_ns():
    while True:
        try:
            inp = input("Nhập ngày sinh (dd/mm/yyyy): ")
            dob = datetime.strptime(inp, "%d/%m/%Y")
            return dob.strftime("%d/%m/%Y")
        except Exception:
            print(">>> Vui lòng nhập giá trị hợp lệ")

def nhap_diem(label):
    while True:
        try:
            inp = float(input("Nhập vào điểm {label}: "))
            if inp < 0 or inp > 10:
                print(">>> Vui lòng nhập giá trị hợp lệ")
            return inp
        except Exception:
            print(">>> Vui lòng nhập giá trị hợp lệ")

class QuanLy:
    def __init__(self):
        self.students = {}

    def nhap(self):
        msv = input("Nhập mã sinh viên: ")
        if msv not in self.students:
            print(f"Mã sinh viên {msv} đã tồn tại.")
            return
        ten = input("Nhập tên sinh viên: ")
        gt = nhap_gt()
        ns = nhap_ns()
        toan = nhap_diem("Toán")
        li = nhap_diem("Lí")
        hoa = nhap_diem("Hóa")
        return SinhVien(msv, ten, gt, ns, toan, li, hoa)

    def them_sv(self, sv):
        if sv is None: return
        self.students[sv.msv] = sv
        print(f"Thêm sinh viên {sv.ten} thành công")

    def in_ds(self):
        if not self.students:
            print("Danh sách chưa có sinh viên nào.")
        else:
            print("Danh sách sinh viên: ")
            for sv in self.students.values():
                print(sv)
    
    def xuat_file(self):
        with open("students.txt", "w", encoding="utf-8") as f:
            for sv in self.students.values():
                f.write(f"{sv}\n")
        print("Đã lưu ra file students.txt.")

    def xuat_file2(self):
        with open("students.csv", "w", newline='', encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Mã SV", "Tên", "Giới tính", "Ngày sinh", "Toán", "Lí", "Hóa", "ĐTB", "Xếp loại"])

            for sv in self.students.values():
                row = [sv.msv, sv.ten, sv.gt, sv.ns, sv.toan, sv.li, sv.hoa, sv.dtb, sv.xl]
                writer.writerow(row)
        print(">>> Đã xuất dữ liệu ra file students.csv thành công.")
    
    def tai_file2(self):
        self.students.clear()
        if not path.exists("students.csv"):
            print(">>> Chưa có file dữ liệu")
            return
        
        try:
            with open("students.csv", "r", newline='', encoding="utf-8") as f:
                reader = csv.reader(f)
                next(reader, None)
                for row in reader:
                    if len(row) < 9:
                        continue
                    msv, ten, gt, ns, toan, li, hoa, dtb,xl = row
                    sv = SinhVien(msv, ten, gt, ns, float(toan), float(li), float(hoa))
                    sv.dtb = float(dtb)
                    sv.xl = xl
                    self.students[msv] = sv
            print("Đã tải dữ liệu thành công.")
        except Exception as e:
            print(e)
    
    def tai_file(self):
        self.students.clear()
        with open("students.txt", "r", encoding="utf-8") as f:
            for line in f:
                tmp = line.split("|")
                if len(tmp) != 9:
                    continue
                msv, ten, gt, ns, toan, li, hoa, dtb, xl = tmp
                sv = SinhVien(msv, ten, gt, ns, float(toan), float(li), float(hoa))
                self.students[msv] = sv
    
    def sua_sv(self, msv):
        if msv not in self.students:
            print(f"Mã sinh viên {msv} không tồn tại.")
            return
        
        sv = self.students[msv]
        while True:
            print("Chọn thông tin sinh viên cần chỉnh sửa:")
            print("1. Tên")
            print("2. Giới tính")
            print("3. Ngày sinh")
            print("4. Điểm Toán")
            print("5. Điểm Lí")
            print("6. Điểm Hóa")
            print("0. Thoát")
            try:
                act = int(input("Chọn trường cần sửa: "))
                if act > 6 or act < 0:
                    print("Vui lòng chọn hành động hợp lệ.")
                if act == 1:
                    sv.ten = input("Nhập vào tên sinh viên: ")
                elif act == 2:
                    sv.gt = nhap_gt()
                elif act == 3:
                    sv.ns = nhap_ns()
                elif act == 4:
                    sv.toan = nhap_diem("Toán")
                elif act == 5:
                    sv.ly = nhap_diem("Lí")
                elif act == 6:
                    sv.hoa = nhap_diem("Hóa")
                elif act == 0:
                    sv.dtb = sv.tinh_dtb()
                    sv.xl = sv.xeploai()
                    self.xuat_file()
                    print("Cập nhật thành công.")
                    break
            except Exception as e:
                print(e)
    
    def xoa_sv(self, msv):
        if msv not in self.students:
            print(f"Mã sinh viên {msv} không tồn tại.")
        else:
            del self.students[msv]
    
    def tim_sv(self, opt, keyword):
        keyword = keyword.lower()
        res = []

        for sv in self.students.values():
            if opt == 1:
                if keyword in sv.msv.lower():
                    res.append(sv)
            elif opt == 2:
                if keyword in sv.ten.lower():
                    res.append(sv)
        
        if not res:
            print("Không tìm thấy kết quả.")
        else:
            print(f"Tìm thấy {len(res)} sinh viên: ")
            for sv in res:
                print(sv)

    def sx_sv(self, opt):
        res = list(self.students.values())
        if opt == 1:
            res = sorted(res, key=lambda st: st.ten)
        else:
            res = sorted(res, key=lambda st: st.dtb, reverse=True)
        for sv in res:
            print(sv)

    def thongke(self):
        res = {"Giỏi": 0, "Khá": 0, "Trung bình": 0, "Yếu": 0}
        for sv in self.students.values():
            res[sv.xl] = res.get(sv.xl, 0) + 1
        for k, v in res:
            print(f"{k}: {v} sinh viên")


if __name__ == "__main__":
    ql = QuanLy()
    act = -1
    if path.exists("students.txt"):
        ql.tai_file()

    while True:
        print("\n" + "=" * 5 + "Quản Lý Sinh Viên" + "=" * 5)
        print("1. Thêm sinh viên")
        print("2. Hiển thị danh sách")
        print("3. Cập nhật thông tin")
        print("4. Xóa sinh viên")
        print("5. Tìm kiếm sinh viên")
        print("6. Sắp xếp danh sách")
        print("7. Thống kê theo học lực")
        print("8. Xuất danh sách ra file")
        print("9. Tải dữ liệu từ file")
        print("0. Thoát chương trình")
        print("=" * 27 + "\n")
        try:

            act = int(input(">>> Chọn hành động (0 -> 9): "))
            if act < 0 or act > 9:
                print(">>> Vui lòng chọn hành động hợp lệ")

            if act == 1:
                sv = ql.nhap()
                ql.them_sv(sv)
            elif act == 2:
                ql.in_ds()
            elif act == 3:
                msv = input("Nhập vào mã sinh viên: ")
                ql.sua_sv(msv)
            elif act == 4:
                msv = input("Nhập vào mã sinh viên: ")
                ql.xoa_sv(msv)
            elif act == 5:
                while True:
                    print("Tiêu chí tìm kiếm: ")
                    print("1. Mã sinh viên")
                    print("2. Tên sinh viên")
                    opt = int(input("Chọn tiêu chí: "))
                    if opt < 1 or opt > 2:
                        print("Vui lòng chọn giá trị hợp lệ")
                        continue
                    keyword = input("Nhập từ khóa: ")
                    ql.tim_sv(opt, keyword)
                    break
            elif act == 6:
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
            elif act == 7:
                ql.thongke()
            elif act == 8:
                # ql.xuat_file()
                ql.xuat_file2()
            elif act == 9:
                # ql.tai_file()
                ql.tai_file2()
            else:
                print(">>> Thoát chương trình")
                break
        except Exception as e:
            print(e)
