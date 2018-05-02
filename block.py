import datetime
# Not actaully using it, was just trying something

class Block:
    def __init__(self, index, transactions, proof,
        previous_hash):
        self.index = index
        self.timestamp = datetime.datetime.now()
        self.transactions = transactions
        self.proof = proof
        self.previous_hash = previous_hash
    
    @property
    def get_data(self):
        """ Returns block object in JSON """
        return {
            'index': self.index,
            'timestamp':self.timestamp,
            'transactions': self.transactions,
            'proof': self.proof,
            'previous_hash': self.previous_hash
        }
