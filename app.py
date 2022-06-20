import json
from web3 import Web3
ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

abi = json.loads('[{"constant":false,"inputs":[{"name":"_greeting","type":"string"}],"name":"setGreeting","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"greet","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"greeting","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"}]')
address = address = web3.toChecksumAddress('0x41AD49ADf15bba7c1eB4F5D1336a120Ac39079B6') 
contract = web3.eth.contract(address=address, abi=abi)
 
# account #3   0xb192710a01E7e73A022282b39B1CfcC23048681 in Ganache
web3.eth.defaultAccount = web3.eth.accounts[2]

tx_hash=contract.functions.setGreeting('XYZ-ABC').transact()
web3.eth.wait_for_transaction_receipt(tx_hash)

print(contract.functions.greet().call())





