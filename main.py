import json
from datetime import datetime

from Crypto.Hash import SHA256


def calculate_hash(data: bytes) -> str:
    h = SHA256.new()
    h.update(data)
    return h.hexdigest()


class Block:
    def __init__(self,
                 timestamp: float,
                 transaction_data: str,
                 previous_blockhash=None):
        self.timestamp = timestamp
        self.transaction_data = transaction_data
        self.previous_blockhash = previous_blockhash

    @property
    def previous_block_cryptohash(self):
        previous_blockhash = "Empty"
        if self.previous_blockhash:
            previous_blockhash = self.previous_blockhash.cryptographic_hash
        return previous_blockhash

    @property
    def cryptographic_hash(self) -> str:
        previous_block_hexdigest = ""
        if self.previous_blockhash:
            previous_block_hexdigest = self.previous_blockhash.cryptographic_hash
        block_content = {
            "Transaction Data": self.transaction_data,
            "Time Stamp": self.timestamp,
            "Previous Block Hash": previous_block_hexdigest
        }
        block_content_bytes = json.dumps(block_content, indent=2).encode('utf-8')
        return calculate_hash(block_content_bytes)


timestamp_0 = datetime.timestamp(datetime.fromisoformat('2011-11-04 00:05:23.111'))
transaction_data_0 = "Albert,Bertrand,30"
block_0 = Block(
    transaction_data=transaction_data_0,
    timestamp=timestamp_0
)

timestamp_1 = datetime.timestamp(datetime.fromisoformat('2011-11-07 00:05:13.222'))
transaction_data_1 = "Albert,Camille,10"
block_1 = Block(
    transaction_data=transaction_data_1,
    timestamp=timestamp_1,
    previous_blockhash=block_0
)

timestamp_2 = datetime.timestamp(datetime.fromisoformat('2011-11-09 00:11:13.333'))
transaction_data_2 = "Bertrand,Camille,5"
block_2 = Block(
    transaction_data=transaction_data_2,
    timestamp=timestamp_2,
    previous_blockhash=block_1
)

timestamp_3 = datetime.timestamp(datetime.fromisoformat('2011-11-09 00:11:10.333'))
transaction_data_3 = "Bertrand,Camilfasdfasle,15"
block_3 = Block(
    transaction_data=transaction_data_3,
    timestamp=timestamp_3,
    previous_blockhash=block_2
)

print(block_0.previous_block_cryptohash)
print(block_1.previous_block_cryptohash)
print(block_2.previous_block_cryptohash)
print(block_3.previous_block_cryptohash)

