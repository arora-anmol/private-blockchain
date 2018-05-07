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
    last_block = blockchain.get_last_block
    print(last_block)
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

    if not data:
        return "No transation data passed", 400

    required = ['sender', 'recipient', 'amount']

    if not (list(data.keys()) == required):
        return 'Missing Value', 400
    
    block_index = blockchain.add_transaction(data['sender'], data['recipient'], data['amount'])
    response = {'message':f'Adding the transaction to block at index: {block_index}'}

    return jsonify(response), 201


@app.route('/nodes/register', methods=['POST'])
def register_nodes():
    nodes = request.get_json().get('nodes')
    if nodes is None:
        return " Need valid nodes to register", 400

    for node in nodes:
        blockchain.register_node(node)

    response = {
        'message': 'Added more nodes to the network'
        'list_of_nodes': list(self.nodes)
    }
    
    return jsonify(response), 201


@app.route('/nodes/resolve', methods=['GET'])
def consensus():
    replaced = blockchain.resolve_conflicts()

    if replaced:
        response = {
            'message': 'This chain was replaced by another chain'
            'new_chain': blockchain.chain
        }
        
        return jsonify(response), 201

    else:
        response = {
            'message': 'This chain was not replaced'
            'chain': blockchain.chain
        }

        return jsonify(response), 200
    
    
@app.route('/chain', methods=['GET'])
def get_chain():
    """ This function is used to get the chain data """
    response = {
        'chain': blockchain.chain,
        'length':len(blockchain.chain)
    }

    return jsonify(response), 200


if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000)
