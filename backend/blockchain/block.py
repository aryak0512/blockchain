import time
from backend.util.cryto_hash import crypto_hash
from backend.config import MINE_RATE
from backend.util.hex_to_binary_conversion import hex_to_binary

GENESIS_DATA = {
    'timestamp' : 1,
    'last_hash' : 'genesis_last_hash',
    'hash' : 'genesis_hash',
    'data' : [],
    'difficulty' : 3,
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
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def to_json(self):
        return self.__dict__

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
        difficulty = Block.adjust_difficulty(last_block=last_block, timestamp=timestamp)
        nonce = 0
        hash = crypto_hash(timestamp, last_hash, data, difficulty, nonce)
        binary_hash = hex_to_binary(hash)
        

        # till the leading number of 0's is not equal to the difficulty
        while binary_hash[0:difficulty] != '0' * difficulty:
            nonce+=1
            timestamp = time.time_ns()
            difficulty = Block.adjust_difficulty(last_block=last_block, timestamp=timestamp)
            hash = crypto_hash(timestamp, last_hash, data, difficulty, nonce)
            binary_hash = hex_to_binary(hash)

        return Block(timestamp=timestamp, last_hash=last_hash, hash=binary_hash,data=data, difficulty=difficulty, nonce=nonce)

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
    
    @staticmethod
    def adjust_difficulty(last_block, timestamp):
        """
        Increase or decrease the difficulty as per mine rate
        """
        if (timestamp - last_block.timestamp) < MINE_RATE :
            return last_block.difficulty + 1
        
        # difficulty should never go negative
        if (last_block.difficulty - 1) > 0:
            return last_block.difficulty - 1 
        
        return 1
    
    @staticmethod
    def is_valid_block(old_block, block):
        """
        Matches the hash computed by the fields with the hash in the block
        and
        Matches the old_hash of current block with hash of last_bloc
        and
        Must have proper proof of work [trailing 0's equal to difficuly]
        and
        Difficultly must only differ by +_ 1 unit
        """
        if old_block.hash == block.last_hash:
            if block.hash[0:block.difficulty] == '0'* block.difficulty:
                if abs(old_block.difficulty - block.difficulty) == 1:
                    hash_computed = crypto_hash(block.timestamp, block.last_hash, block.data, block.difficulty, block.nonce)
                    if hash_computed==block.hash:
                        return True
                    return False
                return False
            return False
        return False

def main():
    genesis_block = Block.genesis()
    # creating a new block
    block = Block.mine_block(genesis_block, 'foo')
    print(block)


if __name__ == "__main__":
    main()
