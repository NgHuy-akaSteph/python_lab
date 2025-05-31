import json
import hashlib

def read_public_key():
    with open('public_key.json', 'r') as f:
        data = json.load(f)
        return int(data['n'])

def read_signature():
    with open('signature.json', 'r') as f:
        data = json.load(f)
        return int(data['signature']), bytes.fromhex(data['salt'])

def read_message():
    with open('message.txt', 'r', encoding='utf-8') as f:
        return f.read()

def verify_signature(message, signature, salt, n):
    salted_msg = message.encode() + salt
    m = int.from_bytes(hashlib.sha256(salted_msg).digest(), 'big') % n
    return pow(signature, 2, n) == m

if __name__ == '__main__':
    message = read_message()
    signature, salt = read_signature()
    n = read_public_key()
    if verify_signature(message, signature, salt, n):
        print("[+] Chữ ký hợp lệ.")
        print("[+]", message)
    else:
        print("[-]Chữ kí không hợp lệ hoặc thông điệp đã bị thay đổi.")
