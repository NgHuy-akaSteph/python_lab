import hashlib
import json
import os
import time
from ecdsa import SigningKey, SECP256k1, VerifyingKey

# Lớp HashUtils cung cấp các phương thức để tính toán hash
class HashUtils:
    @staticmethod
    def sha256(data):
        """Tính toán SHA-256 hash"""
        if isinstance(data, str):
            data = data.encode()
        return hashlib.sha256(data).hexdigest()
        
    @staticmethod
    def double_sha256(data):
        """Tính toán double SHA-256 hash - hash của hash"""
        if isinstance(data, str):
            data = data.encode()
        return hashlib.sha256(hashlib.sha256(data).digest()).hexdigest()
        
    @staticmethod
    def calculate_merkle_root(transactions):
        """Tính toán Merkle root từ danh sách giao dịch
        Merkle root là hash của tất cả các giao dịch trong khối
        Được sử dụng để xác minh tính toàn vẹn của dữ liệu"""
        if not transactions:
            return "0" * 64
            
        tx_hashes = [tx.txid for tx in transactions]
        while len(tx_hashes) > 1:
            if len(tx_hashes) % 2 != 0:
                tx_hashes.append(tx_hashes[-1])
            new_hashes = []
            for i in range(0, len(tx_hashes), 2):
                combined = tx_hashes[i] + tx_hashes[i+1]
                new_hashes.append(HashUtils.double_sha256(combined))
            tx_hashes = new_hashes
        return tx_hashes[0]

# Lớp Block đại diện cho một khối trong blockchain
class Block:
    def __init__(self, index, transactions, previous_hash):
        self.index = index  # Số thứ tự khối
        self.transactions = transactions  # Danh sách giao dịch trong khối
        self.previous_hash = previous_hash  # Hash của khối trước
        self.timestamp = time.time()  # Thời gian tạo khối
        self.nonce = 0  # Số nonce dùng trong proof of work
        self.merkle_root = HashUtils.calculate_merkle_root(transactions)  # Merkle root của các giao dịch
        self.hash = self.calculate_hash()  # Hash của khối
        
    def calculate_hash(self):
        """Tính toán hash của khối dựa trên tất cả thông tin trong khối"""
        block_data = {
            "index": self.index,
            "transactions": [tx.__dict__ for tx in self.transactions],
            "previous_hash": self.previous_hash,
            "timestamp": self.timestamp,
            "nonce": self.nonce,
            "merkle_root": self.merkle_root
        }
        return HashUtils.double_sha256(json.dumps(block_data, sort_keys=True))

# Lớp Blockchain quản lý toàn bộ chuỗi khối
class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]  # Khởi tạo với khối genesis
        self.pending_transactions = []  # Danh sách giao dịch chờ xử lý
        self.consensus = Consensus()  # Cơ chế đồng thuận
        
    def create_genesis_block(self):
        """Tạo khối genesis - khối đầu tiên của blockchain"""
        return Block(0, [], "0")
        
    def add_transaction(self, transaction):
        """Thêm giao dịch mới vào danh sách chờ
        Kiểm tra tính hợp lệ của giao dịch trước khi thêm"""
        # Kiểm tra chữ ký
        if not transaction.verify_signature():
            print("Giao dịch không hợp lệ: Chữ ký không đúng")
            return False
            
        # Bỏ qua kiểm tra số dư nếu là giao dịch SYSTEM
        if transaction.sender != "SYSTEM":
            # Kiểm tra số dư của người gửi
            sender_balance = self.get_balance(transaction.sender)
            if sender_balance < transaction.amount:
                print(f"Giao dịch không hợp lệ: Số dư không đủ ({sender_balance} < {transaction.amount})")
                return False
            
        self.pending_transactions.append(transaction)
        return True
        
    def get_balance(self, address):
        """Tính toán số dư của một địa chỉ bằng cách xem xét tất cả giao dịch"""
        balance = 0.0
        for block in self.chain:
            for tx in block.transactions:
                if tx.receiver == address:
                    balance += tx.amount
                if tx.sender == address:
                    balance -= tx.amount
        return balance
        
    def mine_block(self):
        """Đào khối mới bằng cách giải bài toán proof of work"""
        if not self.pending_transactions:
            print("Không có giao dịch nào để đào")
            return None
            
        previous_block = self.chain[-1]
        new_block = Block(len(self.chain), self.pending_transactions, previous_block.hash)
        
        # Điều chỉnh độ khó
        self.consensus.adjust_difficulty(self)
        
        # Đào khối bằng cách tìm nonce phù hợp
        print(f"Đang đào khối #{new_block.index}...")
        start_time = time.time()
        
        while not self.consensus.validate_proof(new_block):
            new_block.nonce += 1
            new_block.hash = new_block.calculate_hash()
            
        mining_time = time.time() - start_time
        print(f"Đào thành công! Thời gian: {mining_time:.2f}s, Nonce: {new_block.nonce}")
        
        self.chain.append(new_block)
        self.pending_transactions = []
        return new_block
        
    def validate_chain(self):
        """Kiểm tra tính hợp lệ của toàn bộ blockchain"""
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]
            
            # Kiểm tra hash của khối hiện tại
            if current_block.hash != current_block.calculate_hash():
                print(f"Hash không hợp lệ ở khối {i}")
                return False
                
            # Kiểm tra liên kết với khối trước
            if current_block.previous_hash != previous_block.hash:
                print(f"Liên kết không hợp lệ giữa khối {i-1} và {i}")
                return False
                
            # Kiểm tra proof of work
            if not self.consensus.validate_proof(current_block):
                print(f"Proof of work không hợp lệ ở khối {i}")
                return False
                
            # Kiểm tra merkle root
            if current_block.merkle_root != HashUtils.calculate_merkle_root(current_block.transactions):
                print(f"Merkle root không hợp lệ ở khối {i}")
                return False
                
            # Kiểm tra tính toàn vẹn của dữ liệu giao dịch
            for tx in current_block.transactions:
                # Kiểm tra chữ ký của giao dịch
                if not tx.verify_signature():
                    print(f"Chữ ký không hợp lệ ở giao dịch {tx.txid} trong khối {i}")
                    return False
                    
                # Kiểm tra txid của giao dịch
                if tx.txid != tx.calculate_txid():
                    print(f"TXID không hợp lệ ở giao dịch {tx.txid} trong khối {i}")
                    return False
                    
        return True


# Lớp Consensus quản lý cơ chế đồng thuận Proof of Work
class Consensus:
    def __init__(self, difficulty=4):
        self.difficulty = difficulty  # Độ khó ban đầu
        self.target = "0" * difficulty + "f" * (64 - difficulty)  # Mục tiêu hash cần đạt được
        
    def validate_proof(self, block):
        """Kiểm tra proof of work - hash của khối phải bắt đầu bằng số lượng số 0 bằng độ khó"""
        return block.hash[:self.difficulty] == "0" * self.difficulty
        
    def adjust_difficulty(self, blockchain):
        """Điều chỉnh độ khó dựa trên thời gian đào khối
        Nếu đào quá nhanh -> tăng độ khó
        Nếu đào quá chậm -> giảm độ khó"""
        if len(blockchain.chain) < 10:
            return
            
        last_10_blocks = blockchain.chain[-10:] # lấy 10 khối cuối
        time_taken = last_10_blocks[-1].timestamp - last_10_blocks[0].timestamp # tính thời gian đào 10 khối cuối
        expected_time = 10 * 60  # 10 phút cho 10 khối
        
        if time_taken < expected_time / 2:
            self.difficulty += 1
        elif time_taken > expected_time * 2:
            self.difficulty = max(1, self.difficulty - 1) # Giảm độ khó tối thiểu là 1
            
        self.target = "0" * self.difficulty + "f" * (64 - self.difficulty) #

# Lớp Transaction đại diện cho một giao dịch trong blockchain
class Transaction:
    def __init__(self, sender, receiver, amount, sender_public_key=""):
        self.sender = sender  # Địa chỉ người gửi
        self.receiver = receiver  # Địa chỉ người nhận
        self.amount = amount  # Số lượng coin
        self.sender_public_key = sender_public_key  # Khóa công khai của người gửi
        self.timestamp = time.time()  # Thời gian tạo giao dịch
        self.signature = None  # Chữ ký số của giao dịch
        self.txid = self.calculate_txid()  # ID duy nhất của giao dịch
        
    def calculate_txid(self):
        """Tính toán TXID của giao dịch dựa trên thông tin giao dịch"""
        tx_data = {
            "sender": self.sender,
            "receiver": self.receiver,
            "amount": self.amount,
            "timestamp": self.timestamp
        }
        return HashUtils.double_sha256(json.dumps(tx_data, sort_keys=True))
        
    def sign_transaction(self, private_key):
        """Ký giao dịch với khóa riêng của người gửi"""
        if self.sender == "SYSTEM":
            self.signature = "SYSTEM"
            return True
        try:
            sk = SigningKey.from_string(bytes.fromhex(private_key), curve=SECP256k1)
            message = self.calculate_txid().encode()
            self.signature = sk.sign(message).hex()
            return True
        except Exception as e:
            print(f"Lỗi khi ký giao dịch: {e}")
            return False
        
    def verify_signature(self):
        """Xác minh chữ ký của giao dịch bằng khóa công khai"""
        if self.sender == "SYSTEM":
            return True
        if not self.signature or not self.sender_public_key:
            return False
        try:
            vk = VerifyingKey.from_string(bytes.fromhex(self.sender_public_key), curve=SECP256k1)
            message = self.calculate_txid().encode()
            return vk.verify(bytes.fromhex(self.signature), message)
        except Exception as e:
            print(f"Lỗi khi xác minh chữ ký: {e}")
            return False


# Lớp Wallet quản lý ví tiền điện tử
class Wallet:
    def __init__(self, wallet_name="default"):
        self.wallet_name = wallet_name  # Tên ví
        self.wallet_file = os.path.join(os.path.dirname(__file__), "keys", f"{wallet_name}.key")  # File lưu khóa
        self.private_key = self.load_or_generate_key()  # Khóa riêng
        self.public_key = self.get_public_key()  # Khóa công khai
        self.address = self.generate_address()  # Địa chỉ ví
        
    def load_or_generate_key(self):
        """Tải khóa từ file hoặc tạo mới nếu chưa có"""
        if os.path.exists(self.wallet_file):
            with open(self.wallet_file, 'r') as f:
                key = f.read().strip()
                if len(key) == 64:
                    return key
        # Nếu không hợp lệ hoặc không tồn tại, tạo mới
        keys_dir = os.path.dirname(self.wallet_file)
        os.makedirs(keys_dir, exist_ok=True)
        sk = SigningKey.generate(curve=SECP256k1)
        private_key = sk.to_string().hex()
        with open(self.wallet_file, 'w') as f:
            f.write(private_key)
        return private_key
        
    def get_public_key(self):
        """Lấy khóa công khai từ khóa riêng"""
        sk = SigningKey.from_string(bytes.fromhex(self.private_key), curve=SECP256k1)
        return sk.verifying_key.to_string().hex()
        
    def generate_address(self):
        """Tạo địa chỉ ví từ khóa công khai"""
        public_key_bytes = bytes.fromhex(self.public_key)
        return HashUtils.double_sha256(public_key_bytes)[:40]
        
    def get_balance(self, blockchain):
        """Tính toán số dư của ví"""
        return blockchain.get_balance(self.address)
        
    def create_transaction(self, receiver, amount):
        """Tạo giao dịch mới"""
        tx = Transaction(self.address, receiver, amount, self.public_key)
        tx.sign_transaction(self.private_key)
        return tx

# Hàm mô phỏng các loại tấn công vào blockchain
def simulate_attack(blockchain):
    """Mô phỏng các loại tấn công vào blockchain để kiểm tra tính bảo mật"""
    print("\n=== MÔ PHỎNG TẤN CÔNG ===")
    
    # 1. Tấn công thay đổi số lượng coin
    print("\n1. Tấn công thay đổi số lượng coin:")
    if len(blockchain.chain[-1].transactions) > 0:
        original_amount = blockchain.chain[-1].transactions[0].amount
        blockchain.chain[-1].transactions[0].amount = 100.0
        print(f"Đã thay đổi số lượng coin từ {original_amount} lên 100.0")
        print(f"Blockchain hợp lệ sau tấn công? {blockchain.validate_chain()}")
        # Khôi phục lại giá trị cũ
        blockchain.chain[-1].transactions[0].amount = original_amount
    else:
        print("Không có giao dịch nào để tấn công.")
    
    # 2. Tấn công thay đổi người nhận
    print("\n2. Tấn công thay đổi người nhận:")
    if len(blockchain.chain[-1].transactions) > 0:
        original_receiver = blockchain.chain[-1].transactions[0].receiver
        fake_wallet = Wallet("fake_wallet")
        blockchain.chain[-1].transactions[0].receiver = fake_wallet.address
        print(f"Đã thay đổi người nhận từ {original_receiver} thành {fake_wallet.address}")
        print(f"Blockchain hợp lệ sau tấn công? {blockchain.validate_chain()}")
        # Khôi phục lại giá trị cũ
        blockchain.chain[-1].transactions[0].receiver = original_receiver
    else:
        print("Không có giao dịch nào để tấn công.")
    
    # 3. Tấn công thêm giao dịch giả
    print("\n3. Tấn công thêm giao dịch giả:")
    if len(blockchain.chain[-1].transactions) > 0:
        print(f"Số giao dịch trước khi tấn công: {len(blockchain.chain[-1].transactions)}")
        fake_tx = Transaction(
            sender=blockchain.chain[-1].transactions[0].sender,
            receiver="FAKE_ADDRESS",
            amount=50.0,
            sender_public_key=blockchain.chain[-1].transactions[0].sender_public_key
        )
        blockchain.chain[-1].transactions.append(fake_tx)
        print(f"Đã thêm giao dịch giả vào khối")
        print(f"Blockchain hợp lệ sau tấn công? {blockchain.validate_chain()}")
        print(f"Số giao dịch sau khi tấn công: {len(blockchain.chain[-1].transactions)}")
        # Khôi phục lại giá trị cũ
        blockchain.chain[-1].transactions = blockchain.chain[-1].transactions[:-1]
    else:
        print("Không có giao dịch nào để tấn công.")
    
    # 4. Tấn công thay đổi hash của khối
    print("\n4. Tấn công thay đổi hash của khối:")
    if len(blockchain.chain) > 1:
        original_hash = blockchain.chain[-1].hash
        blockchain.chain[-1].hash = "0" * 64
        print(f"Đã thay đổi hash của khối cuối")
        print(f"Blockchain hợp lệ sau tấn công? {blockchain.validate_chain()}")
        # Khôi phục lại giá trị cũ
        blockchain.chain[-1].hash = original_hash
    else:
        print("Không có đủ khối để tấn công.")

# Hàm demo quá trình giao dịch hoàn chỉnh
def demo_complete_transaction():
    print("=== DEMO CHUYỂN COIN TRONG BLOCKCHAIN ===")
    
    # 1. Khởi tạo blockchain
    print("\n1. Khởi tạo blockchain...")
    blockchain = Blockchain()
    print(f"Blockchain đã được tạo với {len(blockchain.chain)} khối (genesis block)")
    
    # 2. Tạo ví
    print("\n2. Tạo ví...")
    wallet_a = Wallet("wallet_a")
    wallet_b = Wallet("wallet_b")
    print(f"Ví A - Địa chỉ: {wallet_a.address}")
    print(f"Ví B - Địa chỉ: {wallet_b.address}")
    
    # 3. Tạo giao dịch tặng 1 coin cho ví A
    print("\n3. Tạo giao dịch tặng 1 coin cho ví A...")
    system_tx = Transaction(
        sender="SYSTEM",
        receiver=wallet_a.address,
        amount=1,
        sender_public_key=""
    )
    system_tx.signature = "SYSTEM"
    blockchain.add_transaction(system_tx)
    blockchain.mine_block()
    print("Đã thêm giao dịch tặng coin cho ví A")
    print(f"Số dư ví A: {wallet_a.get_balance(blockchain)}")
    
    # 4. Ví A gửi 1 coin cho ví B
    print("\n4. Ví A gửi 1 coin cho ví B...")
    tx_a_to_b = wallet_a.create_transaction(wallet_b.address, 1)
    if tx_a_to_b.verify_signature():
        blockchain.add_transaction(tx_a_to_b)
        blockchain.mine_block()
        print("Giao dịch đã được thêm và xác nhận")
    else:
        print("Giao dịch không hợp lệ: Chữ ký không đúng")
    
    # 5. Kiểm tra số dư
    print("\n5. Số dư các ví:")
    print(f"Số dư ví A: {wallet_a.get_balance(blockchain)}")
    print(f"Số dư ví B: {wallet_b.get_balance(blockchain)}")
    
    # 6. Kiểm tra và hiển thị thông tin blockchain
    print("\n6. Thông tin blockchain:")
    print(f"Số khối trong chuỗi: {len(blockchain.chain)}")
    print(f"Số giao dịch trong khối mới: {len(blockchain.chain[-1].transactions)}")
    if len(blockchain.chain) >= 2:
        print(f"Hash của khối trước: {blockchain.chain[-2].previous_hash}")
    else:
        print("Chưa có đủ 2 block để lấy hash của khối trước.")
    print(f"Blockchain hợp lệ? {blockchain.validate_chain()}")
    
    # 7. Mô phỏng tấn công
    simulate_attack(blockchain)


if __name__ == "__main__":
    demo_complete_transaction() 