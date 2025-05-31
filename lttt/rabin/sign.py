import json
import hashlib
import os

def read_private_key():
    with open('private_key.json', 'r') as f:
        key = json.load(f)
        return int(key['p']), int(key['q'])

def is_quadratic_residue(m, p, q):
    return pow(m, (p-1)//2, p) == 1 and pow(m, (q-1)//2, q) == 1

def rabin_sign(message, p, q):
    n = p * q
    # Tạo mã băm cho thông điệp
    trials = 0
    while True:
        salt = os.urandom(8)
        salted_msg = message.encode() + salt
        m = int.from_bytes(hashlib.sha256(salted_msg).digest(), 'big') % n
        if is_quadratic_residue(m, p, q):
            break
        trials += 1
        if trials > 1000:
            raise Exception("Không tìm được thông điệp phù hợp để ký.")

    # Tính căn bậc hai modulo p và q
    mp = pow(m, (p + 1) // 4, p)
    mq = pow(m, (q + 1) // 4, q)
    # Tính modulo nghịch đảo của p theo q và q theo p
    yp = pow(p, -1, q)
    yq = pow(q, -1, p)
    r = (yp * p * mq + yq * q * mp) % n

    return r, salt.hex()

if __name__ == '__main__':
    message = "Đây là thông điệp bí mật"
    p, q = read_private_key()
    signature, salt = rabin_sign(message, p, q)

    with open('signature.json', 'w') as f:
        json.dump({
            'signature': str(signature),
            'salt': salt
        }, f)

    with open('message.txt', 'w', encoding='utf-8') as f:
        f.write(message)

    print("[+] Chữ ký đã được tạo và lưu vào signature.json")
    print("[+] Thông điệp đã được lưu vào message.txt")
