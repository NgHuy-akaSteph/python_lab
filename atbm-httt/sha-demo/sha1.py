import hashlib

# Hàm left_rotate dùng để quay trái một số nguyên 32-bit
def left_rotate(x, c):
    return ((x << c) | (x >> (32 - c))) & 0xffffffff

def sha1(message):
    # Các hằng số khởi tạo
    h0 = 0x67452301
    h1 = 0xEFCDAB89
    h2 = 0x98BADCFE
    h3 = 0x10325476
    h4 = 0xC3D2E1F0

    # Chuyển message thành bytes nếu là string
    if isinstance(message, str):
        message = message.encode()  # mặc định là utf-8

    # Đệm message
    ml = len(message) * 8 # Độ dài message ban đầu
    message += b'\x80' # Thêm 1 bit '1' vào cuối message, b'' là bytes string
    # Thêm các bit '0' vào cho đến khi độ dài của message là 448 bit
    # Để dành 8 bytes = 64 bit cuối cùng cho độ dài ban đầu của message
    while (len(message) + 8) % 64 != 0:
        message += b'\x00'
    message += ml.to_bytes(8, 'big')

    # Xử lý từng block 512 bits
    for i in range(0, len(message), 64): # 64 bytes = 512 bits
        block = message[i : (i + 64)] # Dùng slicing để lấy block

        # Tạo message schedule array w[0..79]
        w = []

        for j in range(16):
            # Lấy lần lượt 4 bytes từ block
            # Chuyển thành 32-bit int bằng cách dùng int.from_bytes() voi byteorder là 'big' - big-endian
            # Chuyển đổi 16 từ đầu thành các int 32-bit và lưu vào w dưới dạng nhị phân
            w.append(int.from_bytes(block[j * 4 : j * 4 + 4], 'big'))

        # Mở rộng w từ 16 thành 80 phần tử
        for j in range(16, 80):
            w.append(left_rotate(w[j - 3] ^ w[j - 8] ^ w[j - 14] ^ w[j - 16], 1))

        # Khởi tạo giá trị hash cho block này
        a = h0
        b = h1
        c = h2
        d = h3
        e = h4

        # Vòng lặp chính của SHA-1
        for j in range(80):
            if 0 <= j <= 19:
                f = (b & c) ^ ((~b) & d)
                k = 0x5A827999
            elif 20 <= j <= 39:
                f = b ^ c ^ d
                k = 0x6ED9EBA1
            elif 40 <= j <= 59:
                f = (b & c) ^ (b & d) ^ (c & d)
                k = 0x8F1BBCDC
            else:
                f = b ^ c ^ d
                k = 0xCA62C1D6

            temp = (left_rotate(a, 5) + f + e + k + w[j]) & 0xffffffff # & 0xffffffff để giữ 32 bits
            e = d
            d = c
            c = left_rotate(b, 30)
            b = a
            a = temp

        # Thêm giá trị hash của block này vào kết quả
        h0 = (h0 + a) & 0xffffffff
        h1 = (h1 + b) & 0xffffffff
        h2 = (h2 + c) & 0xffffffff
        h3 = (h3 + d) & 0xffffffff
        h4 = (h4 + e) & 0xffffffff

    # Kết hợp các giá trị hash thành kết quả cuối cùng
    return '%08x%08x%08x%08x%08x' % (h0, h1, h2, h3, h4)

def sha1_file(file_path):
    with open(file_path, 'rb') as f:
        file_content = f.read()
    return sha1(file_content)

def hash_message_sha1(message):
    sha1_hash = hashlib.sha1()
    sha1_hash.update(message.encode('utf-8'))
    return sha1_hash.hexdigest()

if __name__ == "__main__":
    input_message = input("Enter the message to hash: ")
    hashed_message = sha1(input_message)
    print(f"Hashed message by my function: {hashed_message}")
    print(f"Hashed message by built-in function: {hash_message_sha1(input_message)}")
    print(f"Hashed message by file: {sha1_file('/atbm-httt/sha-demo/pdf/shattered-1.pdf')}")
    print(f"Hashed message by file: {sha1_file('/atbm-httt/sha-demo/pdf/shattered-2.pdf')}")
