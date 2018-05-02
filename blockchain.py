""" Primitive Python implementation of blockchain, 
    using Proof of Work consensus protocol """



from block import Block # Not actually using it

import datetime
import json
import hashlib

class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        #Creating the genesis block
        self.add_genesis_block(proof=100, previous_hash=1)

    def add_genesis_block(self, proof, previous_hash):
        self.chain.append({
            'index'
        })
    
    def _create_block(self, proof, previous_hash, index=None):
        if index:
            index = len(self.chain)+1 
        return {
            'index': index
            'timestamp': datetime.datetime.now(),
            'transactions': self.current_transactions,
            'proof': proof
            'previous_hash': previous_hash
        }

    def add_block(self):
        """Add a new block to blockchain """
        index = len(self.chain)+1
        block = {
            'index': index.
            'timestamp': datetime.datetime.now(),
            'transactions': self.current_transactions,
            'proof': proof
            'previous_hash': self.chain[-1].hash()
        }
        self.chain.append(block)

    def add_transaction(self, sender, recipient, amount):
        """ Add transaction to be mined in the next block """

        self.current_transactions.append({
            'sender': sender,
            'recipient':recipient,
            'amount': amount
        })

    @staticmethod
    def hash(block):
        pass
    
    @property
    def get_last_block(self):
        return self.chain[-1]


