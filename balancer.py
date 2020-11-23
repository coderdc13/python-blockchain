from bit import wif_to_key

key = wif_to_key("")

## this code taken directly from lecture led by Instructor GS...

## from class addresses = [""]

## from class outputs = []

## from class for address in addresses:
## from class    outputs.append((address, 0.000001, "btc"))

## from class print(key.send(outputs))

print(key.get_balance("btc"))
print(key.balance_as("usd"))
print(key.get_transactions())
print(key.get_unspent())

