import os


def format_dob(dob):
    d, m, y = dob.split("/")
    if len(d) == 1:
        d = f"0{d}"
    if len(m) == 1:
        m = f"0{m}"
    return f"{d}/{m}/{y}"


class Student:
    cnt = 1

    def __init__(self, name, gender, dob, toan, ly, hoa):
        self.id = f"SV{Student.cnt:03d}"
        Student.cnt += 1
        self.name = name
        self.gender = gender
        self.dob = dob
        self.toan = toan
        self.ly = ly
        self.hoa = hoa
        self.dtb = self.avg_score()
        self.xeploai = self.stage()

    def avg_score(self):
        avg = (self.toan + self.ly + self.hoa) / 3
        return round(avg, 2)

    def stage(self):
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
        return f"{self.id}|{self.name}|{self.gender}|{self.dob}|{self.toan}|{self.ly}|{self.hoa}|{self.dtb}|{self.xeploai})"


def input_student():
    name = input("Nhập tên sinh viên: ")
    gender = input("Nhập giới tính (Nam/Nữ): ")
    dob = input("Nhập vào ngày sinh: ")
    toan = float(input("Nhập điểm Toán: "))
    ly = float(input("Nhập điểm Lý: "))
    hoa = float(input("Nhập điểm Hóa: "))
    return Student(name, gender, format_dob(dob), toan, ly, hoa)


def nhap_diem_hop_le(label):
    """Hàm đảm bảo người dùng nhập điểm từ 0-10"""
    while True:
        try:
            diem = float(input(f"Nhập vào điểm {label}: "))
            if 0 <= diem <= 10:
                return diem
            else:
                print("Lỗi: Điểm phải nằm trong khoảng từ 0 đến 10. Vui lòng nhập lại.")
        except ValueError:
            print("Lỗi: Vui lòng nhập một số thực hợp lệ.")


class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, st):
        self.students.append(st)
        print("Đã thêm sinh viên thành công.")

    def display_students(self):
        if len(self.students) == 0:
            print("Không có sinh viên nào.")
        else:
            print("")
            for student in self.students:
                print(student)

    def search_by_name(self, name):
        result = [st for st in self.students if name.lower() in st.name.lower()]
        for st in result:
            print(st)

    def update_student(self, sid):
        for i, st in enumerate(self.students):
            if st.id == sid:
                new_st = input_student()
                new_st.id = sid
                self.students[i] = new_st
                print(f"Cập nhật sinh viên {sid} thành công")
                return
        print(f"Không tìm thấy sinh viên {sid}")

    def delete_student(self, sid):
        for st in self.students:
            if st.id == sid:
                self.students.remove(st)
        print(f"Xóa thành công sinh viên {sid}")

    def sort_student(self):
        self.students.sort(key=lambda st: st.dtb, reverse=True)
        for st in self.students:
            print(st)

    def stats_by_classification(self):
        counts = {"Giỏi": 0, "Khá": 0, "Trung Bình": 0, "Yếu": 0}
        for st in self.students:
            counts[st.xeploai] = counts.get(st.xeploai, 0) + 1
        for label, total in counts.items():
            print(f"{label}: {total}")

    def save_to_file(self, path):
        with open(path, "w", encoding="utf-8") as f:
            for s in self.students:
                f.write(f"{s}\n")
        print(f"Lưu thành công vào file: {path}")

    def load_from_file(self, path):
        if not os.path.exists(path):
            print(f"Tệp {path} không tồn tại")
            return

        self.students.clear()
        Student.cnt = 1
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split("|")
                if len(parts) != 9:
                    continue
                sid, name, gender, dob, toan, ly, hoa, dtb, xeploai = parts
                stu = Student(name, gender, dob, float(toan), float(ly), float(hoa))
                stu.id = sid
                stu.dtb = float(dtb)
                stu.xeploai = xeploai
                self.students.append(stu)
                Student.cnt = max(Student.cnt, int(sid[2:]) + 1)
        print(f"Tải dữ liệu thành công từ: {path}")


if __name__ == "__main__":
    manager = StudentManager()
    action = -1

    while True:
        print("\n================ CHƯƠNG TRÌNH QUẢN LÝ SINH VIÊN ================")
        print("1. Thêm sinh viên")
        print("2. Hiển thị danh sách")
        print("3. Tìm kiếm sinh viên")
        print("4. Cập nhật thông tin")
        print("5. Xóa sinh viên")
        print("6. Sắp xếp danh sách (mặc định là giảm dần theo dtb)")
        print("7. Thống kê xếp loại")
        print("8. Lưu danh sách ra file")
        print("9. Đọc danh sách từ file")
        print("0. Thoát chương trình")
        print("===============================================================")

        try:
            action = int(input("Chọn chức năng: "))
            if action > 9 or action < 0:
                print("Vui lòng chọn chức năng từ 0 đến 9.")
                continue

            if action == 0:
                print("Thoát chương trình.")
                break

            elif action == 1:
                student = input_student()
                manager.add_student(student)

            elif action == 2:
                manager.display_students()

            elif action == 3:
                name = input("Nhập vào tên sinh viên:")
                manager.search_by_name(name)

            elif action == 4:
                sid = input("Nhập vào id sinh viên cần sửa:")
                manager.update_student(sid)

            elif action == 5:
                sid = input("Nhập vào id sinh viên cần xóa:")
                manager.delete_student(sid)

            elif action == 6:
                manager.sort_student()

            elif action == 7:
                manager.stats_by_classification()

            elif action == 8:
                manager.save_to_file("students.txt")

            elif action == 9:
                manager.load_from_file("students.txt")
                manager.display_students()

        except ValueError:
            print("Vui lòng nhập một số hợp lệ.")
            continue
