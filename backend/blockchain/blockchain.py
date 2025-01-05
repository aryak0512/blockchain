from backend.blockchain.block import Block

class Blockchain:
    """
    A public ledger of transactions
    """
    def __init__(self):
        self.chain = [Block.genesis()]

    def __repr__(self):
        return f'Blockchain object : {self.chain}'
    
    def to_json(self):
        return list(map(lambda block : block.to_json(), self.chain))
    
    def add_block(self, data):
        """
        Retrives the last block from the blockchain and mines a new block and attaches it to the chain
        """
        last_block = self.chain[-1]
        # create the block
        block = Block.mine_block(last_block=last_block, data=data)
        self.chain.append(block)


    @staticmethod
    def is_chain_valid(chain):

        if chain[0] != Block.genesis():
            raise Exception('The gensis of chain is invalid!')

        for i in range (1, len(chain)):
            block = chain[i]
            last_block = chain[i-1]
            Block.is_valid_block(old_block=last_block, block=block)

def main():
    blockchain = Blockchain()
    blockchain.add_block('Block1')
    blockchain.add_block('Block2')
    print(blockchain)

if __name__ == "__main__":
    main()