import time

def mine_block(last_block, data):
    """
    Creating a block is called mining and involves solving a computing challenge
    We need the previous block reference to get value of last_hash
    @returns a new block
    """
    # defining params for new block
    timestamp = time.time_ns()
    last_hash = last_block.hash
    hash = f'{timestamp}-{last_hash}'
    return Block(timestamp=timestamp, last_hash=last_hash, hash=hash,data=data)

def genesis():
    """
    This is the first block of the blockchain and generally a bunch of hardcoded fields
    """
    return Block(1, 'genesis_last_hash', 'genesis_hash', [])

class Block:
    """
    A block is a unit of storage
    """
    def __init__(self, timestamp, last_hash, hash, data):
        self.timestamp = timestamp
        self.last_hash = last_hash
        self.hash = hash
        self.data = data

    def __repr__(self):
        return (
            'Block ('
                f'data : {self.data}, '
                f'last_hash : {self.last_hash}, '
                f'hash : {self.hash}, '
                f'timestamp : {self.timestamp}'
            ')'
        )
    

def main():
    genesis_block = genesis()
    # creating a new block
    block = mine_block(genesis_block, 'foo')
    block2 = mine_block(block, 'foo1')
    print(block)
    print(block2)

if __name__=="__main__":
    main()
