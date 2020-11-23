import subprocess
import json


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
#w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
w3 = Web3(Web3.HTTPProvider(os.getenv('http://127.0.0.1:8545', 'http://localhost:8545')))
# calling mnemonic environment variable
mnemonic = os.getenv('MNEMONIC')
w3.middleware_onion.inject(geth_poa_middleware, layer=0)


#command = 'php derive -g --mnemonic="wagon rail round impuls donor radr escape harsh series" --cols=path,address,privkey,pubkey --format=json'
## command = 'php hd-wallet-derive/hd-wallet-derive.php -g --mnemonic="wagon rail round impuls donor radr escape harsh series" --cols=path,address,privkey,pubkey --format=json'

## p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
## (output, err) = p.communicate()
## p_status = p.wait()
# hd-wallet-derive/hd-wallet-derive.php

#print(p_status)
## keys = json.loads(output)
## print(keys)
## print(keys[0]['address'])

#above was overflow, monday after halloween, also, above works just like in example... 
## classdelay... def derive_wallets(coin):
def derive_wallets(coin):
    command = f'php ./hd-wallet-derive/hd-wallet-derive.php -g --mnemonic="{mnemonic}" --cols=path,address,privkey,pubkey --coin="{coin}" --numderive=2 --format=json'
    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    p_status = p.wait()
    keys = json.loads(output) #newprob
    return(keys)

coins = {
    ETH: derive_wallets(ETH), #newprob
    BTCTEST: derive_wallets(BTCTEST)
}
print(coins)
# private is 'cRNMeTebY9hS45npxocksNu8rmJPssE4vZfeTStCboxkH9xzmtVU'
INDEX = 0
print(coins[ETH][INDEX]['privkey'])


def priv_key_to_account(coin, priv_key):
    if coin == ETH:
        return Account.privateKeyToAccount(priv_key)
    else:
        return PrivateKeyTestnet(priv_key)

def create_tx(coin, account, to, amount):
    if coin == ETH:
        gasEstimate = w3.eth.estimateGas(
            {
                "from": account.address, 
                #"from": account,
                "to": to, 
                "value": amount
            }
        )
        return {
            "from": account.address,
            #"from": account,
            "to": to, 
            "value": amount,
            "gasPrice": w3.eth.gasPrice,
            "gas": gasEstimate,
            "nonce": w3.eth.getTransactionCount(account.address),
            #"nonce": w3.eth.getTransactionCount(account),
            # "chainID": 450
        }
    else:
        #return PrivateKeyTestnet.prepare_transaction(account, [(to, amount, BTC)])
        return PrivateKeyTestnet.prepare_transaction(account.address, [(to, amount, BTC)])

def send_tx(coin, account, to, amount):
    tx = create_tx(coin, account, to, amount)
    signed = account.sign_transaction(tx)
    if coin == ETH:
        return w3.eth.sendRawTransaction(signed.rawTransaction)
    else:
        return NetworkAPI.broadcast_tx_testnet(signed)
    #print(result.hex())
    
from bit import wif_to_key




'''
account_1 = priv_key_to_account(BTCTEST, coins[BTCTEST][0]['privkey'])
send_tx(coin=BTCTEST, account=account_1, to=coins[BTCTEST][1]['address'], amount=0.00001)



key1 = wif_to_key(coins[BTCTEST][0]['privkey'])

key2 = wif_to_key(coins[BTCTEST][1]['privkey'])

print(key1.get_balance("btc"))
print(key1.balance_as("usd"))
print(key2.get_balance("btc"))
print(key2.balance_as("usd"))

'''

# account_alpha = priv_key_to_account(ETH, coins[ETH][0]['privkey'])
# send_tx(coin=ETH, account=account_alpha, to=coins[ETH][1]['address'], amount=100000)

'''

key1 = wif_to_key(coins[ETH][0]['privkey'])

key2 = wif_to_key(coins[ETH][1]['privkey'])

print(key1.get_balance("eth"))
print(key1.balance_as("usd"))
print(key2.get_balance("eth"))
print(key2.balance_as("usd"))

'''
