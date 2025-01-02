import time
from backend.util.cryto_hash import crypto_hash

GENESIS_DATA = {
    'timestamp' : 1,
    'last_hash' : 'genesis_last_hash',
    'hash' : 'genesis_hash',
    'data' : [],
    'difficulty' : 4,
    'nonce' : 1
}

class Block:
    """
    A block is a unit of storage
    """
    def __init__(self, timestamp, last_hash, hash, data, difficulty, nonce):
        self.timestamp = timestamp
        self.last_hash = last_hash
        self.hash = hash
        self.data = data
        self.difficulty = difficulty
        self.nonce = nonce

    def __repr__(self):
        return (
            'Block ('
                f'data : {self.data}, '
                f'last_hash : {self.last_hash}, '
                f'hash : {self.hash}, '
                f'timestamp : {self.timestamp}, '
                f'difficulty : {self.difficulty}, '
                f'nonce : {self.nonce}'
            ')'
        )
    
    @staticmethod
    def mine_block(last_block, data):
        """
        Creating a block is called mining and involves solving a computing challenge
        We need the previous block reference to get value of last_hash

        We mine till the leading number of 0's is equal to the difficulty

        @returns a new block
        """
        # defining params for new block
        timestamp = time.time_ns()
        last_hash = last_block.hash
        difficulty = last_block.difficulty
        nonce = 0
        hash = crypto_hash(timestamp, last_hash, data, difficulty, nonce)

        while hash[0:difficulty] != '0' * difficulty:
            nonce+=1
            timestamp = time.time_ns()
            hash = crypto_hash(timestamp, last_hash, data, difficulty, nonce)

        return Block(timestamp=timestamp, last_hash=last_hash, hash=hash,data=data, difficulty=difficulty, nonce=nonce)

    @staticmethod
    def genesis():
        """
        This is the first block of the blockchain and generally a bunch of hardcoded fields
        """
        return Block(
            GENESIS_DATA['timestamp'],
            GENESIS_DATA['last_hash'],
            GENESIS_DATA['hash'],
            GENESIS_DATA['data'],
            GENESIS_DATA['difficulty'],
            GENESIS_DATA['nonce']
        )

def main():
    genesis_block = Block.genesis()
    # creating a new block
    block = Block.mine_block(genesis_block, 'foo')
    print(block)


if __name__ == "__main__":
    main()
