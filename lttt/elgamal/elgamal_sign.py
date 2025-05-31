from Crypto.Util import number
import json
import hashlib

def elgamal_sign(message, private_key, public_key):
    p = public_key["p"]
    g = public_key["g"]
    x = private_key["x"]
    h = int(hashlib.sha256(message.encode()).hexdigest(), 16) % p
    while True:
        k = number.getRandomRange(2, p-1)
        if number.GCD(k, p-1) == 1:
            break
    r = pow(g, k, p)
    k_inv = number.inverse(k, p-1) # Nghich đảo của k mod (p-1)
    s = (h - x * r) * k_inv % (p-1)
    return r, s

# Đọc khóa bí mật và khóa công khai từ file
with open("private_key.json", "r") as f:
    private_key = json.load(f)
with open("public_key.json", "r") as f:
    public_key = json.load(f)

# Tạo thông điệpvà chữ ký
message = "Đây là thông điệp bí mật từ Sender"
r, s = elgamal_sign(message, private_key, public_key)

# Lưu chữ ký và thông điệp vào file
with open("message.txt", "w") as f:
    f.write(message)
with open("signature.json", "w") as f:
    json.dump({"r": r, "s": s}, f)

print("[+] Đã ký thông điệp thành công")
print("[+] Chữ ký đã được tạo và lưu vào signature.json")
print("[+] Thông điệp đã được lưu vào message.txt")