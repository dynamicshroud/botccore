# BOTC v1.0
# made by vortex

import binascii, config, json, requests
from os import path

from botc import *
from txndata import *
from flask import Flask, jsonify, request

from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA

botc = Flask(__name__)

# List of nodes that this current node is aware of.
known_nodes = []

@botc.route('/txn/new', methods=['POST'])
def newTransaction():
	txndata = binascii.unhexlify(bytes(request.form["txndata"], "utf-8"))
	signature = binascii.unhexlify(bytes(request.form["signature"], "utf-8"))
	
	verifier = PKCS1_v1_5.new(RSA.importKey(binascii.unhexlify(struct.unpack(pfmt, txndata)[0])))

	h = SHA.new(txndata)
	if verifier.verify(h, signature):
		bc.make_block(txndata)
		for node in known_nodes:
			requests.post(node + '/new', data = {"txndata": binascii.hexlify(txndata)})
		return jsonify(status = "ok")
	else:
		return jsonify(status = "notok")


@botc.route('/announce')
def announceBlockchain():
	return jsonify(blockchain = [i.parse() for i in bc.blocks])

@botc.route('/new', methods=['POST'])
def newBlock():
	txndata = binascii.unhexlify(bytes(request.form["txndata"], "utf-8"))

	if bc.make_block(txndata):
		return jsonify(status = "ok")
	else:
		return jsonify(status = "notok")

@botc.route('/register')
def registerUser():
	if request.remote_addr in known_nodes:
		return jsonify(registered = "already"), 200
	known_nodes.append(request.remote_addr)
	if request.remote_addr in known_nodes:
		return jsonify(registered = "ok"), 200

@botc.route('/nodes')
def getNodes():
	return jsonify(nodes = known_nodes)

@botc.route('/find/<hash>')
def findBlock(hash):
	return jsonify(bc.find_block(hash))

if __name__ == '__main__':
	print("""
	BOTCNode 1.0 by vortex
	Written with <3	
	""")
	if path.isfile(config.KNOWNHOSTSFILE):
		with open(config.KNOWNHOSTSFILE, "r") as f:
			for line in f:
				known_nodes.append(line.strip())
			f.close()

	print(known_nodes)
	botc.run(config.HOST, config.PORT)