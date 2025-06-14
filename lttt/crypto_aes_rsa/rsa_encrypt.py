import math
import time
from collections import Counter
from bitstring import BitArray
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
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

def rsa_experiment(plaintext, key_size, max_plaintext_size):
    """Thực nghiệm RSA với độ dài khóa và bản rõ tối đa chỉ định."""
    print(f"\n=== Thực nghiệm với RSA ({key_size}-bit, plaintext {max_plaintext_size} byte) ===")
    rsa_key = RSA.generate(key_size)
    public_key = rsa_key.publickey()

    # Entropy của plaintext
    plaintext_entropy = calculate_entropy(plaintext)
    print(f"Entropy của bản gốc: {plaintext_entropy:.2f} bit/byte")

    # Entropy của khóa công khai
    public_key_bytes = public_key.n.to_bytes((public_key.n.bit_length() + 7) // 8, 'big')
    key_entropy = calculate_entropy(public_key_bytes)
    print(f"Entropy của khóa công khai RSA: {key_entropy:.2f} bit/byte")

    # Mã hóa
    start_time = time.time()
    cipher = PKCS1_OAEP.new(public_key)
    ciphertext = cipher.encrypt(plaintext)
    elapsed_time = time.time() - start_time
    ciphertext_entropy = calculate_entropy(ciphertext)
    print(f"Entropy của bản mã RSA: {ciphertext_entropy:.2f} bit/byte")
    print(f"Thời gian mã hóa: {elapsed_time:.6f} giây")

    # Hiệu ứng tuyết lở
    modified_plaintext = flip_bit(plaintext, 0)
    modified_ciphertext = cipher.encrypt(modified_plaintext)
    diff_bits = hamming_distance(ciphertext, modified_ciphertext)
    total_bits = len(ciphertext) * 8
    changed_percentage = (diff_bits / total_bits) * 100
    print(
        f"Số bit thay đổi khi đảo 1 bit plaintext: {diff_bits} / {total_bits} ({changed_percentage:.2f}%)")

if __name__ == "__main__":
    rsa_plaintext_2048 = get_plaintext(214)
    rsa_plaintext_4096 = get_plaintext(470)
    rsa_experiment(rsa_plaintext_2048, 2048, 214)
    rsa_experiment(rsa_plaintext_4096, 4096, 470)