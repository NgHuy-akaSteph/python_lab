import json
from Crypto.Util import number

def generate_prime(bits=512):
    while True:
        p = number.getPrime(bits)
        if p % 4 == 3:
            return p

def generate_keys():
    p = generate_prime()
    q = generate_prime()
    n = p * q

    with open('private_key.json', 'w') as f:
        json.dump({'p': str(p), 'q': str(q)}, f)

    with open('public_key.json', 'w') as f:
        json.dump({'n': str(n)}, f)

    print("[+] Khóa công khai được tạo và lưu vào public_key.json")
    print("[+] Khóa riêng được tạo và lưu vào private_key.json")

if __name__ == '__main__':
    generate_keys()
