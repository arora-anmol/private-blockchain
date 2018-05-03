""" 
    This module has the code for the blockchain node
    It's made using Flask, which is a web framework for python
"""


import hashlib
import json

from flask import Flask, jsonify, request
from uuid import uuid4

from blockchain import Blockchain


app = Flask(__name__)

node_identifier = str(uuid4()).replace('-', '')

blockchain = Blockchain()


@app.route('/mine', methods=['GET'])
def mine():
    """ This function is used to mine the block with current transactions"""
    last_block = blockchain.get_last_block()
    last_proof = last_block['proof']
    proof = blockchain.proof_of_work(last_proof)

    blockchain.add_transaction(sender=0, recipient=node_identifier, amount=1)
    block = blockchain.add_block(proof)
    block['message'] = 'New block added'

    return jsonify(block), 200


@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    """ This function is used to add a transaction to the current transactions list"""

    data = request.get_json()
    required = ['sender', 'recipient', 'amount']
    if not (list(data.keys()) == required):
        return 'Missing Value', 400
    
    block_index = blockchain.add_transaction(data['sender'], data['recipient'], data['amount'])
    response = {'message':f'Adding the transaction to block at index: {block_index}'}
    
    return jsonify(response), 200


@app.route('/chain', method=['GET'])
def get_chain():
    """ This function is used to get the chain data """
    response = {
        'chain':blockchain.chain,
        'length':len(blockchain.chain)
    }

    return jsonify(response), 200


if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000)
