
import time
from backend.blockchain.blockchain import Blockchain
from backend.config import SECOND


times = []
blockchain = Blockchain()
for i in range(1000):
    t1 = time.time_ns()
    blockchain.add_block(i)
    t2 = time.time_ns()
    times.append((t2-t1) / SECOND)
    latest_block = blockchain.chain[-1]
    print(f'Time taken to mine current block : {(t2-t1) / SECOND}')
    print(f'Current block difficulty : {latest_block.difficulty}')
    print(f'Current average time : {sum(times) / len(times)}')
    print("=========================================")

