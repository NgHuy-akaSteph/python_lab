import hashlib

def hash_file(file_path):
    """Tính giá trị băm SHA-1 của một file."""
    sha1_hash = hashlib.sha1()
    with open(file_path, "rb") as f:
        # Đọc file theo từng khối 4096 bytes
        for byte_block in iter(lambda: f.read(4096), b""):
            sha1_hash.update(byte_block)
    return sha1_hash.hexdigest()

# Hàm này sẽ so sánh giá trị băm của hai file
def compare_files(file1, file2):
    hash1 = hash_file(file1)
    hash2 = hash_file(file2)

    print(f"Hash của {file1}: {hash1}")
    print(f"Hash của {file2}: {hash2}")

    if hash1 == hash2:
        print("Hai file có giá trị băm giống nhau.")
    else:
        print("Hai file có giá trị băm khác nhau.")

if __name__ == '__main__':
    input_file1 = "H:/python-workspace/sha-demo/pdf/shattered-1.pdf"
    input_file2 = "H:/python-workspace/sha-demo/pdf/shattered-2.pdf"
    compare_files(input_file1, input_file2)