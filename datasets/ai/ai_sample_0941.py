import hashlib
import json

# define a block in the blockchain
class Block:
    def __init__(self, index, data, timestamp, prev_hash):
        self.index = index
        self.data = data
        self.timestamp = timestamp
        self.prev_hash = prev_hash
        self.hash = self.hash_it()

    # generates a SHA256 based on the contents of the block
    def hash_it(self):
        sha = hashlib.sha256()
        block_data = str(self.index) + str(self.data) + str(self.timestamp) + str(self.prev_hash) 
        sha.update(block_data.encode())
        return sha.hexdigest()

# defines a blockchain
class Blockchain:
    def __init__(self):
        self.chain = []

    # adds a block to the blockchain
    def add_block(self, data):
        data = self.parse_data(data)
        index = len(self.chain)
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        prev_hash = self.chain[-1].hash if self.chain else '0'

        self.chain.append(Block(index, data, timestamp, prev_hash))

    # records a user's name and age in the block data
    def parse_data(self, data):
        user_data = {
            'name': data['name'],
            'age': data['age']
        }
        return json.dumps(user_data)