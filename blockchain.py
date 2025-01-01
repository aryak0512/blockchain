from block import Block
import time

class Blockchain:
    """
    A public ledger of transactions
    """
    def __init__(self):
        self.chain = []

    def __repr__(self):
        return f'Blockchain object : {self.chain}'
    
    def add_block(self, block):
        self.chain.append(block)

def main():
    ts = time.clock_gettime_ns
    block = Block(ts, 'last_hs', 'hash', 'd1')

if __name__=="__main__":
    main()