from bit import wif_to_key

key = wif_to_key("cRNMeTebY9hS45npxocksNu8rmJPssE4vZfeTStCboxkH9xzmtVU")


print(key.get_balance("btc"))
print(key.balance_as("usd"))

print(key.get_transactions())

print(key.get_unspents())



##later addresses = ["mrLu5P2hLXdJUNn8UwSwGVnuv6kMApvyUs"]









##lateroutputs = []

##laterfor address in addresses:
##later    outputs.append((address, 0.000001, "btc"))

##laterprint(key.send(outputs))