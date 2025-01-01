from block import Block

class Blockchain:
    """
    A public ledger of transactions
    """
    def __init__(self):
        self.chain = [Block.genesis()]

    def __repr__(self):
        return f'Blockchain object : {self.chain}'
    
    def add_block(self, data):
        """
        Retrives the last block from the blockchain and mines a new block and attaches it to the chain
        """
        last_block = self.chain[-1]
        # create the block
        block = Block.mine_block(last_block=last_block, data=data)
        self.chain.append(block)

def main():
    blockchain = Blockchain()
    blockchain.add_block('Block1')
    blockchain.add_block('Block2')
    print(blockchain)

if __name__ == "__main__":
    main()