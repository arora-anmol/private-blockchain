""" Primitive Python implementation of blockchain, 
    using Proof of Work consensus protocol """



from block import Block # Not actually using it

import datetime
import json
import hashlib as hasher

class Blockchain:
    def __init__(self):
        """ Initialize the blockchain """
        self.chain = []
        self.current_transactions = []
        #Creating the genesis block
        self.chain.append(self._create_block(proof=100, previous_hash=1, index=0))


    def _create_block(self, proof, previous_hash, index=None):
        """ Creates and returns a new block using the current transactions """
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
        block = self._create_block(proof, self.chain[-1].hash())
        self.chain.append(block)
        self.current_transactions[:] = []   #Empty the list of current transactions once they are added to the block


    def add_transaction(self, sender, recipient, amount):
        """ Add transaction to be mined in the next block """

        self.current_transactions.append({
            'sender': sender,
            'recipient':recipient,
            'amount': amount
        })


    @staticmethod
    def hash(block):
        """ Returns SHA 256 hash of the passed block (JSON Object) """
        block_string = json.dumps(block, sort_keys=True).encode()
        return hasher.sha256(block_string).hexdigest()

    
    @property
    def get_last_block(self):
        """ Gets the last block added to the blockchain """
        return self.chain[-1]

    def proof_of_work(self, last_proof):
        proof = 0
        while not valid_proof(last_proof, proof):
            proof = proof+1
        
        return proof

    @staticmethod
    def valid_proof(self, last_proof, proof):
        guess_string  = f'{last_proof}{proof}'.encode()
        guess_hash = hasher.sha256(guess_string).hexdigest()

        return guess_hash[:4] == '0000'

