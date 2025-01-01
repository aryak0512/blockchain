from backend.util.cryto_hash import crypto_hash

def test_crypto():
    
    assert crypto_hash('foo') == 'b2213295d564916f89a6a42455567c87c3f480fcd7a1c15e220f17d7169a790b'

    # The change in sequence of operands must not change the hash value
    assert crypto_hash(1, 'two', [3]) == crypto_hash('two', 1, [3])