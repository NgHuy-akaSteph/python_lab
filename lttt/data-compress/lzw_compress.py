def lzw_pure_compress(data):
    if not data:
        return []
    
    # Khởi tạo từ điển với các ký tự ASCII cơ bản
    dictionary = {chr(i): i for i in range(256)}
    next_code = 256
    result = []
    current = ""
    
    # Duyệt qua từng ký tự trong dữ liệu
    for char in data:
        current_plus_char = current + char
        if current_plus_char in dictionary:
            current = current_plus_char
        else:
            result.append(dictionary[current])
            dictionary[current_plus_char] = next_code
            next_code += 1
            current = char
    
    # Thêm mã cuối cùng nếu còn
    if current:
        result.append(dictionary[current])
    
    return result

def lzw_codes_to_bytes(codes):
    # Chuyển danh sách mã số thành bytes
    # Sử dụng số bit tối thiểu để mã hóa các mã
    import math
    if not codes:
        return b""
    # Tính số bit cần thiết để mã hóa các mã
    max_code = max(codes) if codes else 0
    bits_needed = max(8, math.ceil(math.log2(max_code + 1)))
    # Chuyển đổi mã thành chuỗi nhị phân
    binary = "".join(format(code, f"0{bits_needed}b") for code in codes)
    # Đảm bảo độ dài của chuỗi nhị phân là bội số của 8
    padded_binary = binary + "0" * (8 - len(binary) % 8) if len(binary) % 8 != 0 else binary
    # Chuyển đổi chuỗi nhị phân thành bytes
    return bytes(int(padded_binary[i:i+8], 2) for i in range(0, len(padded_binary), 8))