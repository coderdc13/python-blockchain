from web3 import Web3


from constants import *
import os
from dotenv import load_dotenv
import subprocess
import json
from eth_account import Account
from bit import PrivateKeyTestnet
from web3 import Web3
from web3.middleware import geth_poa_middleware
from bit.network import NetworkAPI

load_dotenv()

w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

print(w3.eth.blockNumber)

print(w3.eth.getBalance("0x14E77e8dE86498E0fB5Ad53Bc0A1Bb2627C898a0"))
# 0x14E77e8dE86498E0fB5Ad53Bc0A1Bb2627C898a0 is the node one account with the enormous balance of practice


# print(w3.eth.getBalance("0x31Bf78837e4062A257c83D6BE07055e2b13450DE"))
# directly above, the 0x31Bf78837e4062A257c83D6BE07055e2b13450DE is the account of the account w the parallel in Kovan and trial_five
# access 0x31Bf78837... with  0x859b790442216b1141b78c648d5c676a0b5baa0f7bf58f671faaecc60aa6a3ad as private key 


mnemonic = os.getenv('MNEMONIC')

priv_key= os.getenv('PRIVATE_KEY')
# private key of 0x31Bf78837e4062A257c83D6BE07055e2b13450DE account

print(mnemonic)
print(priv_key)

account_one = Account.from_key(priv_key)
print(account_one.address)

def create_raw_tx(account, recipient, amount):
    gasEstimate = w3.eth.estimateGas({"from":account.address, "to":recipient, "value":amount})
    return {
        "from": account.address,
        "to": recipient,
        "value": amount,
        "gasPrice": w3.eth.gasPrice,
        "gas": gasEstimate,
        "nonce": w3.eth.getTransactionCount(account.address),
    }

def send_tx(account, recipient, amount):
    tx = create_raw_tx(account, recipient, amount)
    signed_tx = account.sign_transaction(tx)
    result = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
    print(result.hex())
    return(result.hex())

#send_tx(account_one, "0xD4dB3B15E17903CB28d5fF1Aee2BEdA4BF76ec46", 5)
# directly above is the wallet made by keystore 0xD4dB3B15E17903CB28d5fF1Aee2BEdA4BF76ec46 
# alt ab 5pm 0x511a29a374181c442c0c99ff4273491ce09a932aa6f17a027965aea15efe11d3

# print(w3.eth.getTransactionReceipt("0x511a29a374181c442c0c99ff4273491ce09a932aa6f17a027965aea15efe11d3"))

#send_tx(account_one, "0x14E77e8dE86498E0fB5Ad53Bc0A1Bb2627C898a0", 1)
# doing above ab 726pm

print(w3.eth.getTransactionReceipt("0x511a29a374181c442c0c99ff4273491ce09a932aa6f17a027965aea15efe11d3"))

# next try 0x8bd3497599454a40b0d6d1b4d1e2dd053ea31412eb9dbd52104d94d2e61256ec

# print(w3.eth.getTransactionReceipt("0x8bd3497599454a40b0d6d1b4d1e2dd053ea31412eb9dbd52104d94d2e61256ec"))
