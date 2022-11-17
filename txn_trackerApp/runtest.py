from web3 import Web3

ganache_url = 'HTTP://127.0.0.1:7545'
web3 = Web3(Web3.HTTPProvider(ganache_url))
account_1 = '0x89aB180B100D396d6FFCFCd468969E97799bB245'
private_key1 = 'd3d679d75a22c64fd6326dea6430eb8eb83f811b7af1a8000cc24f2fa6245301'

print(web3.isConnected())
account_2 = '0x9CB4be349c2F37e003b1BAb588033e7f12770eeC'
private_key2 = '6bc57d59895e0cbfd0782bc01f11fe2ef38a438b99e1b6f831c3d94b3b892911'

nonce = web3.eth.getTransactionCount(account_2)

#build a transaction in a dictionary
tx = {
    'nonce': nonce,
    'to': account_1,
    'value': web3.toWei(3, 'ether'),  # One ether = 1,000,000,000,000,000,000 wei (10e18) 
    'gas': 200000,
    'gasPrice': web3.toWei('50', 'gwei')
}

#sign the transaction
signed_tx = web3.eth.account.sign_transaction(tx, private_key2)

#send transaction
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)

#get transaction hash
print("transaction hash",web3.toHex(tx_hash))

# print the latest block number
print("block numbers:",web3.eth.block_number)
