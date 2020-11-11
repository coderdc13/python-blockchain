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

# calling mnemonic environment variable
mnemonic = os.getenv('MNEMONIC')


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

INDEX = 0
print(coins[ETH][INDEX]['privkey'])

w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

def priv_key_to_account(coin, privkey):
    if coin == ETH:
        return Account.privateKeyToAccount(priv_key)
    elif coin == BTCTEST:
        return PrivateKeyTestnet(priv_key)

def create_tx(coin, account, to, amount):
    if coin == ETH:
        gasEstimate = w3.eth.estimateGas(
            {
                "from": account.address, 
                "to": to, 
                "value": amount
            }
        )
        return {
            "from": account.address,
            "to": to, 
            "value": amount,
            "gasPrice": w3.eth.gasPrice,
            "gas": gasEstimate,
            "nonce": w3.eth.getTransactionCount(account.address),
            # "chainID": 450
        }
    elif coin == BTCTEST:
        return PrivateKeyTestnet.prepare_transaction(account.address, [(to, amount, BTC)])

def send_tx(coin, account, recipient, amount):
    tx = create_tx(coin, account, to, amount)
    signed = account.sign_transaction(tx)
    if coin == ETH:
        return w3.eth.sendRawTransaction(signed.rawTransaction)
    elif coin == BTCTEST:
        return NetworkAPI.broadcast_tx_testnet(signed)
    print(result.hex())
    