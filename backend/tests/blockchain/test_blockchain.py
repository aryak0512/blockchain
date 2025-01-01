from backend.blockchain.block import Block,GENESIS_DATA
from backend.blockchain.blockchain import Blockchain

def test_blockchain():
    blockchain = Blockchain()
    assert blockchain.chain[0].hash == GENESIS_DATA['hash']

def test_add_block():
    blockchain = Blockchain()
    data = 'test-data'
    blockchain.add_block(data=data)
    assert blockchain.chain[-1].data == data