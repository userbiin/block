import hashlib
import time

class Block: 
    def __init__(self, index, previous_hash, timestamp, data):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = self.calculate_hash()
        
    def calculate_hash(self):
        data_to_hash = f"{self.index}{self.previous_hash}{self.timestamp}{self.data}"
        return hashlib.sha256(data_to_hash.encode()).hexdigest()

class Blockchain: 
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        
    def create_genesis_block(self):
        return Block(0, "0", time.time(), "Genesis Block")
    
    def get_latest_block(self):
        return self.chain[-1]
    
    def add_block(self, data):
        time.sleep(1)
        previous_block = self.get_latest_block()
        new_block = Block(len(self.chain), previous_block.hash, time.time(), data)
        self.chain.append(new_block)
        
    def is_chain_vaild(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]
            
            if current_block.hash != current_block.calculate_hash():
                return False
            
            if current_block.previous_hash != previous_block.hash:
                return False
            
        return True
    
my_blockchain = Blockchain()  # genesis_block(시작 블록) 생성됨 -> 블록체인 생성 
my_blockchain.add_block("First transaction data") # data가 들어간 블록 생성 
my_blockchain.add_block("Second transaction data")
my_blockchain.add_block("Third transaction data")

for block in my_blockchain.chain:
    print(f"Index : {block.index}")
    print(f"Current Hash: {block.hash}")
    print(f"Previous Hash: {block.previous_hash}")
    print(f"Timestamp: {block.timestamp}")
    print(f"Data: {block.data}")
    print(f"-" * 40)
    
print("Is blockchain vaild?", my_blockchain.is_chain_vaild())  #블록체인 유효성 검증 

            