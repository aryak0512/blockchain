from backend.blockchain.block import Block, GENESIS_DATA
import time
from backend.config import MINE_RATE

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

def test_quickly_mined_block():
    last_block = Block.mine_block(Block.genesis(), 'foo')
    mined_block = Block.mine_block(last_block=last_block, data='foo')
    # the mined block is generated almost instantly so its difficultly must be increased by 1
    assert mined_block.difficulty == last_block.difficulty + 1

def test_slowly_mined_block():
    last_block = Block.mine_block(Block.genesis(), 'foo')
    time.sleep(2)
    mined_block = Block.mine_block(last_block=last_block, data='foo')
    # the mined block is generated almost instantly so its difficultly must be increased by 1
    assert mined_block.difficulty == last_block.difficulty - 1

def test_slowly_mined_block_limits_to_1():
    last_block = Block(
        timestamp=time.time_ns(),
        last_hash='',
        hash='',
        data='',
        difficulty=1,
        nonce=0
    )
    time.sleep(2)
    mined_block = Block.mine_block(last_block=last_block, data='foo')
    # the mined block is generated almost instantly so its difficultly must be increased by 1
    assert mined_block.difficulty == 1