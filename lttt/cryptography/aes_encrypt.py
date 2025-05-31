import math
import time
from collections import Counter
from bitstring import BitArray
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def calculate_entropy(data):
    if len(data) == 0:
        return 0
    freq = Counter(data)
    entropy = 0
    for count in freq.values():
        probability = count / len(data)
        entropy -= probability * math.log2(probability)
    return entropy

def hamming_distance(data1, data2):
    """Tính khoảng cách Hamming (số bit khác nhau)."""
    b1 = BitArray(data1)
    b2 = BitArray(data2)
    return (b1 ^ b2).count(True)


def flip_bit(data, bit_position):
    """Đảo 1 bit tại vị trí bit_position."""
    data_array = bytearray(data)
    byte_pos = bit_position // 8
    bit_pos = bit_position % 8
    data_array[byte_pos] ^= (1 << bit_pos)
    return bytes(data_array)

def reduce_entropy(data, replacement_byte=0x00, replace_ratio=0.5):
    """Giảm entropy bằng cách thay thế một số byte dữ liệu bằng 0x00."""
    data_array = bytearray(data)
    replace_count = int(len(data_array) * replace_ratio)
    for i in range(replace_count):
        data_array[i] = replacement_byte
    return bytes(data_array)

def get_plaintext(size):
    """Tạo plaintext ngẫu nhiên với kích thước chỉ định."""
    return reduce_entropy(get_random_bytes(size))


def pad_plaintext(plaintext):
    """Đệm plaintext để chia hết cho 16 byte."""
    pad_len = 16 - (len(plaintext) % 16)
    return plaintext + bytes([pad_len] * pad_len)


def aes_experiment(plaintext, mode_name, mode):
    """Thực nghiệm AES với chế độ chỉ định."""
    print(f"\n=== Thực nghiệm với AES ({mode_name}) ===")
    key = get_random_bytes(32) # 256-bit

    # Entropy của plaintext
    plaintext_entropy = calculate_entropy(plaintext)
    print(f"Entropy của bản gốc: {plaintext_entropy:.2f} bit/byte")

    # Entropy của khóa
    key_entropy = calculate_entropy(key)
    print(f"Entropy của khóa AES (256-bit): {key_entropy:.2f} bit/byte")

    # Mã hóa
    start_time = time.time()
    if mode == AES.MODE_ECB:
        ciphertext = AES.new(key, AES.MODE_ECB).encrypt(pad_plaintext(plaintext))
    else:  # CBC
        iv = get_random_bytes(16)
        ciphertext = AES.new(key, AES.MODE_CBC, iv).encrypt(pad_plaintext(plaintext))
    elapsed_time = time.time() - start_time
    ciphertext_entropy = calculate_entropy(ciphertext)
    print(f"Entropy của bản mã AES: {ciphertext_entropy:.2f} bit/byte")
    print(f"Thời gian mã hóa: {elapsed_time:.6f} giây")

    # Hiệu ứng tuyết lở
    modified_plaintext = flip_bit(plaintext, 0)
    if mode == AES.MODE_ECB:
        modified_ciphertext = AES.new(key, AES.MODE_ECB).encrypt(pad_plaintext(modified_plaintext))
    else:
        modified_ciphertext = AES.new(key, AES.MODE_CBC, iv).encrypt(pad_plaintext(modified_plaintext))
    diff_bits = hamming_distance(ciphertext, modified_ciphertext)
    total_bits = len(ciphertext) * 8
    changed_percentage = (diff_bits / total_bits) * 100
    print(
        f"Số bit thay đổi khi đảo 1 bit plaintext: {diff_bits} / {total_bits} ({changed_percentage:.2f}%)")

if __name__ == "__main__":
    # Tạo plaintext ngẫu nhiên với kích thước 1024 byte
    aes_plaintext = get_plaintext(1024)
    aes_experiment(aes_plaintext, "ECB", AES.MODE_ECB)
    aes_experiment(aes_plaintext, "CBC", AES.MODE_CBC)