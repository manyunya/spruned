from dataclasses import dataclass

import typing

INT4_MAX = 4294967295


@dataclass
class BlockHeader:
    data: bytes
    hash: bytes
    height: typing.Optional[int] = None

    @property
    def prev_block_hash(self):
        return self.data and self.data[4:36][::-1]

    def as_dict(self):
        return {
            'data': self.data,
            'height': self.height,
            'hash': self.hash
        }


@dataclass
class Block:
    hash: bytes
    data: bytes
    height: int

    @property
    def header(self):
        return BlockHeader(
            data=self.data[:80],
            height=self.height,
            hash=self.hash
        )

    @property
    def size(self):
        return len(self.data)


@dataclass
class UTXO:
    hash: bytes
    height: int
    amount: int
    script: bytes
    witness: bytes
