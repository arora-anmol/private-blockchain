""" Primitive Python implementation of blockchain, 
    using Proof of Work consensus protocol """



# from block import Block # Not actually using it

import datetime
import json
import hashlib as hasher
import requests

from urllib.parse import urlparse

class Blockchain:
    def __init__(self):
        """ Initialize the blockchain """
        self.chain = []
        self.current_transactions = []
        self.nodes = set()      #To maintain a set of nodes in the distributed network
        #Creating the genesis block
        genesis_block = self._create_block(proof=100, previous_hash=1, index=1)
        self.chain.append(genesis_block)


    def register_node(self, address):
        parsed_url = urlparse(address)
        self.nodes.add(parsed_url)


    def _create_block(self, proof, previous_hash, index=None):
        """ Creates and returns a new block using the current transactions """
        if not index:
            index = len(self.chain)+1
        return {
            'index': index,
            'timestamp': str(datetime.datetime.now()),
            'transactions': self.current_transactions.copy(),
            'proof': proof,
            'previous_hash': previous_hash
        }


    def add_block(self, proof):
        """Add a new block to blockchain """
        block = self._create_block(proof, Blockchain.hash(self.chain[-1]))
        self.current_transactions = []   #Empty the list of current transactions once they are added to the block
        self.chain.append(block)

        return block 


    def add_transaction(self, sender, recipient, amount):
        """ Add transaction to be mined in the next block """

        self.current_transactions.append({
            'sender': sender,
            'recipient':recipient,
            'amount': amount
        })
        return self.chain[-1]['index']+1


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
        """
            Proof of Work Algorithm:
            After appending the last proof with a test proof, 
            if the hash produces 4 leading 0s, the test proof becomes the valid proof for the block
        """
        proof = 0
        while not Blockchain.valid_proof(last_proof, proof):
            proof = proof+1
        
        return proof


    @staticmethod
    def valid_proof(last_proof, proof):
        """ Check if the proof is valid i.e, has 4 leading zeroes"""
        guess_string  = f'{last_proof}{proof}'.encode()
        guess_hash = hasher.sha256(guess_string).hexdigest()

        return guess_hash[:4] == '0000'


    def valid_chain(self, chain):
        """ We check for hash of block and Proof of Work, to make sure the chain is valid"""
        # not checking for genesis block here
        for i in range(1,len(chain)-1):
            if self.hash(chain[i]) != chain[i+1]['previous_hash']:
                return False
            
            if not self.valid_proof(chain[i-1]['proof'], chain[i]['proof']):
                return False
        
        return True


    def resolve_conflicts(self):
        """ For resolving the conflicts, the longest chain with
            all valid blocks replaces the current chain
        """
        neighbours = self.nodes
        max_length = len(self.chain)
        dominant_chain = []

        for node in neighbours:
            response = requests.get(f'{node.geturl()}/chain')

            if response.status_code == 200:
                chain = response.json()['chain']
                chain_length = response.json()['length']
            
                if chain_length > max_length and self.valid_chain(chain):
                    max_length = chain_length
                    dominant_chain = chain

        if dominant_chain:
            self.chain = dominant_chain
            return True

        return False



