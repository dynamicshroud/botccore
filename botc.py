import hashlib, struct, time, binascii
from txndata import *

class Block:
	def __init__(self, txndata):
		self.index = 0
		self.txndata = txndata

		self.prev_hash = ""
		self.timestamp = time.ctime()

		self.hash = hashlib.sha256(bytes("{}{}{}".format(self.txndata, self.prev_hash, self.timestamp), 'utf-8')).hexdigest()

	def parse(self):
		return {"index": self.index, "txndata": get_txndata(self.txndata), "hash": self.hash, "previous_hash": self.prev_hash, "timestamp": self.timestamp}

class Blockchain:
	def __init__(self):
		self.blocks = []
		self.make_genesis_block()
	
	def make_genesis_block(self):
		genesis_block = Block(make_txndata('0' * 324, '0' * 324, 0))
		self.blocks.append(genesis_block)

	def make_block(self, txndata):
		block = Block(txndata)
		block.index = self.blocks[-1].index + 1
		block.prev_hash = self.blocks[-1].hash

		self.blocks.append(block)

	def find_block(self, hash):
		for i in self.blocks:
			if hash == i.hash:
				return i.parse()
			else:
				return self.blocks[0].parse()

bc = Blockchain()