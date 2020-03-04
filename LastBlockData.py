import json
import random
import string
import time


class Block:
    def __init__(self, index):
        self.BlockIndex = index
        self.TimeStamp = time.time()
        self.PrevHash = ''.join(random.choice(string.ascii_lowercase + '1234567890') for i in range(64))
        self.Nonce = 0
        self.Transactions = []


class Transaction:
    def __init__(self, transactionIndex):
        self.TransactionIndex = f'{transactionIndex}'
        self.SenderAddress = ''.join(random.choice(string.ascii_lowercase + '1234567890') for i in range(64))
        self.RecipientAddress = ''.join(random.choice(string.ascii_lowercase + '1234567890') for i in range(64))
        self.Amount = round(random.uniform(0, 1), 16)
        self.Message = "testMessage"


def redo_json():
    transactions = []
    block = Block(0)

    for i in range(0, 100):
        transaction = Transaction(i)
        transactions.append(
            [
                json.dumps(transaction.__dict__),
                {
                    "signature": ''.join(random.choice(string.ascii_lowercase + '1234567890') for i in range(64))
                }
            ]
        )

    block.Transactions = transactions
    with open('data.json', 'w') as jsonfile:
        json.dump(block.__dict__, jsonfile)



if __name__ == '__main__':
    redo_json()
