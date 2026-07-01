import hashlib
import json

class Blockchain:

 def __init__(self):
 self.chain = []
 self.transactions = []

 def create_block(self, nonce, previous_hash):
 block = {
 'block_number': len(self.chain) + 1,
 'timestamp': self._current_timestamp(),
 'nonce': nonce,
 'previous_hash': previous_hash
 }
 self.chain.append(block)
 return block

 def _current_timestamp(self):
 return round(time.time() * 1000)

 def hash_block(self, block):
 string_object = json.dumps(block, sort_keys=True)
 block_string = string_object.encode()
 raw_hash = hashlib.sha256(block_string)
 hex_hash = raw_hash.hexdigest()
 return hex_hash