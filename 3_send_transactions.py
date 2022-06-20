from web3 import Web3

ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

account_1 = '0x688303CdBE86f2eC49be731Cd681651191B8Fb15' # Fill me in
account_2 = '0x636f055F7285D6D0F8bAfa561c83a2F2920b15aD' # Fill me in
private_key = '41a92c34139ffbbfa5dc9e0833c1eaae7b51f39cf3df026a67fd3d78993f8bf7' # Fill me in

nonce = web3.eth.getTransactionCount(account_1)

tx = {
    'nonce': nonce,
    'to': account_2,
    'value': web3.toWei(5, 'ether'),
    'gas': 2000000,
    'gasPrice': web3.toWei('50', 'gwei'),
}

signed_tx = web3.eth.account.signTransaction(tx, private_key)

tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)

print(web3.toHex(tx_hash))
