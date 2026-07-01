import hashlib
import json

# We will use SHA256 as our hashing function
def sha256(data):
    hash_function = hashlib.sha256()
    hash_function.update(data.encode('utf-8'))
    return hash_function.hexdigest()

# Create a class for each block
class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = sha256(f'{self.index}{self.timestamp}{self.data}{self.previous_hash}')

# Create a class for the blockchain
class Blockchain:
    def __init__(self):
        self.chain = []

    def add_block(self, data):
        previous_hash = self.chain[-1].hash if len(self.chain) > 0 else None
        block = Block(len(self.chain), data['timestamp'], data['data'], previous_hash)
        self.chain.append(block)

    # This method will return the entire blockchain in JSON format
    def get_chain(self):
        return json.dumps([b.__dict__ for b in self.chain], indent=2)