from flask import Flask, jsonify
from backend.blockchain.blockchain import Blockchain

app = Flask(__name__)
blockchain = Blockchain()

@app.route('/')
def route_default():
    return 'Welcome to blockchain'

@app.route('/blockchain')
def route_blockchain():
    return jsonify(blockchain.to_json())

@app.route('/blockchain/mine')
def route_mine_block():
    data = 'stubbed-transaction-data'
    blockchain.add_block(data)
    return jsonify(blockchain.chain[-1].to_json())

app.run(port=8009)