import hashlib
import json

# Define the Block class
class Block:
 def __init__(self, index, timestamp, data, previous_hash):
 self.index = index
 self.timestamp = timestamp
 self.data = data
 self.previous_hash = previous_hash
 self.hash = self.hash_block()

 # Create the hash of the block contents
 def hash_block(self):
 sha = hashlib.sha256()
 sha.update((str(self.index) + 
 str(self.timestamp) + 
 str(self.data) + 
 str(self.previous_hash)).encode('utf-8'))
 return sha.hexdigest()

# Create the blockchain
def create_blockchain():
 blockchain = [create_genesis_block()]
 previous_block = blockchain[0]

 # Add blocks for each item in the list of transactions
 for i in range(1, len(blockchain_transactions)):
 block_to_add = next_block(previous_block, blockchain_transactions[i])
 blockchain.append(block_to_add)
 previous_block = block_to_add

# Print the blockchain
def print_blockchain():
 for block in blockchain:
 block_index = str(block.index)
 block_timestamp = str(block.timestamp)
 block_data = str(block.data)
 block_hash = block.hash