# Tài Liệu Blockchain Demo

## 1. Tổng Quan

File `blockchain_me.py` triển khai một blockchain đơn giản với các tính năng cơ bản như:

- Quản lý giao dịch và ví
- Đào khối (mining)
- Xác thực chữ ký số
- Bảo mật bằng Merkle Tree
- Mô phỏng các cuộc tấn công

## 2. Các Class Chính

### 2.1 HashUtils

```python
class HashUtils:
    @staticmethod
    def sha256(data)
    @staticmethod
    def double_sha256(data)
    @staticmethod
    def calculate_merkle_root(transactions)
```

- Cung cấp các hàm băm cơ bản
- Triển khai Merkle Tree để xác minh tính toàn vẹn của giao dịch

### 2.2 Consensus

```python
class Consensus:
    def __init__(self, difficulty=4)
    def validate_proof(self, block)
    def adjust_difficulty(self, blockchain)
```

- Quản lý độ khó của việc đào khối
- Tự động điều chỉnh độ khó dựa trên thời gian đào khối

### 2.3 Transaction

```python
class Transaction:
    def __init__(self, sender, receiver, amount, sender_public_key="")
    def calculate_txid(self)
    def sign_transaction(self, private_key)
    def verify_signature(self)
```

- Đại diện cho một giao dịch trong blockchain
- Hỗ trợ ký và xác thực chữ ký số
- Tính toán ID duy nhất cho mỗi giao dịch

### 2.4 Block

```python
class Block:
    def __init__(self, index, transactions, previous_hash)
    def calculate_hash(self)
```

- Đại diện cho một khối trong blockchain
- Lưu trữ danh sách giao dịch
- Tính toán hash và Merkle root

### 2.5 Blockchain

```python
class Blockchain:
    def __init__(self)
    def create_genesis_block(self)
    def add_transaction(self, transaction)
    def get_balance(self, address)
    def mine_block(self)
    def validate_chain(self)
```

- Quản lý chuỗi khối
- Xử lý giao dịch và đào khối
- Kiểm tra tính hợp lệ của blockchain

### 2.6 Wallet

```python
class Wallet:
    def __init__(self, wallet_name="default")
    def load_or_generate_key(self)
    def get_public_key(self)
    def generate_address(self)
    def get_balance(self, blockchain)
    def create_transaction(self, receiver, amount)
```

- Quản lý ví và khóa
- Tạo và ký giao dịch
- Kiểm tra số dư

## 3. Các Tính Năng Bảo Mật

### 3.1 Merkle Tree

- Sử dụng để xác minh tính toàn vẹn của giao dịch
- Mỗi khối chứa một Merkle root
- Cho phép xác minh nhanh chóng một giao dịch

### 3.2 Chữ Ký Số

- Sử dụng ECDSA với đường cong SECP256k1
- Mỗi giao dịch được ký bằng khóa riêng
- Xác thực bằng khóa công khai

### 3.3 Proof of Work

- Điều chỉnh độ khó tự động
- Bảo vệ chống tấn công Sybil
- Đảm bảo thời gian tạo khối ổn định

## 4. Demo và Mô Phỏng Tấn Công

### 4.1 Demo Giao Dịch

```python
def demo_complete_transaction():
    # Khởi tạo blockchain
    # Tạo ví
    # Tạo giao dịch
    # Đào khối
    # Kiểm tra số dư
```

### 4.2 Mô Phỏng Tấn Công

```python
def simulate_attack(blockchain):
    # Tấn công thay đổi số lượng coin
    # Tấn công thay đổi người nhận
    # Tấn công thêm giao dịch giả
    # Tấn công thay đổi hash
```

## 5. Cách Sử Dụng

1. Khởi tạo blockchain:

```python
blockchain = Blockchain()
```

2. Tạo ví:

```python
wallet = Wallet("my_wallet")
```

3. Tạo giao dịch:

```python
tx = wallet.create_transaction(receiver_address, amount)
```

4. Thêm giao dịch vào blockchain:

```python
blockchain.add_transaction(tx)
```

5. Đào khối:

```python
blockchain.mine_block()
```

## 6. Yêu Cầu Hệ Thống

- Python 3.x
- Thư viện: ecdsa, hashlib, json, os, time

## 7. Hạn Chế

- Chưa hỗ trợ mạng P2P
- Chưa có cơ chế đồng bộ hóa
- Chưa có cơ chế lưu trữ dữ liệu
- Chưa hỗ trợ smart contract

## 8. Hướng Phát Triển

- Thêm cơ chế đồng bộ hóa
- Triển khai mạng P2P
- Thêm cơ chế lưu trữ dữ liệu
- Hỗ trợ smart contract
- Cải thiện hiệu suất
