import threading
import time

def mining(difficulty, start):
    threads = []
    nonce = start

    # Create threads
    for _ in range(10):
        t = threading.Thread(target=mining_thread,
        args=(difficulty, nonce))
        threads.append(t)
        nonce = nonce + 100

    # Start threads
    for thread in threads:
        thread.start()
  
    # Join threads
    for thread in threads:
        thread.join()

    # Main mining loop
def mining_thread(difficulty, start):
    nonce = start
    while True:
        hash = generate_hash(nonce)
  
        # Check if the hash meets the difficulty
        if hash[:difficulty] == '0' * difficulty:
            print('Hash found!')
            return nonce
  
        nonce = nonce + 1