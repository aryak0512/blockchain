from backend.blockchain.block import Block, GENESIS_DATA

def test_genesis():

    genesis_block = Block.genesis()
    
    # simple instance check
    assert isinstance(genesis_block, Block)

    # check all attributes of the block object
    for k,v in GENESIS_DATA.items():
       assert getattr(genesis_block, k) == v

def test_mine_block():
    data = 'test-data'
    block = Block.mine_block(Block.genesis(), data)
    assert block.data == data
    assert block.last_hash == GENESIS_DATA['hash']
    assert block.hash[0:block.difficulty] == '0'*block.difficulty
