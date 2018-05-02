from block import Block

class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_transactions = []

    def add_block(self):
        pass

    def add_transaction(self, sender, receipient, amount):
        """ Add transaction to be mined in the next block """
        pass

    @staticmethod
    def hash(block):
        pass
    
    @property
    def get_last_block(self):
        return self.chain[-1]


