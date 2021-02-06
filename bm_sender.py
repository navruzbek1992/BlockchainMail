### REPLY TO MESSAGES ###

from web3 import Web3
import requests
import json
import codecs
import time
import winsound

# w3 = Web3(Web3.WebsocketProvider("ws://127.0.0.1:8545", websocket_timeout=200))

print("-------------------------------------------------")
print("Extracting owner, contract and receiver related info")

with open("credentials.json", "r") as json_data:
    credentials = json.load(json_data)

# ## for dev purpose
# answer = input("Are you owner? (yes or no) ")
#
# if answer == "yes":
#     ownerAddress = credentials["ownerAddress"]
#     ownerPrivateKey = credentials["ownerPrivateKey"]
# else:
#     ownerAddress = credentials["friendAddress"]
#     ownerPrivateKey = credentials["friendPrivateKey"]

ownerAddress = credentials["ownerAddress"]
ownerPrivateKey = credentials["ownerPrivateKey"]
bmAddress = credentials["BMAddress"]
infuraLink = credentials["infuraLink"]
w3 = Web3(Web3.WebsocketProvider(infuraLink, websocket_timeout=200))

with open("BlockchainMail.json", "r") as outfile:
    bm_json = json.load(outfile)

bm_contract_instance = w3.eth.contract(address=bmAddress, abi=bm_json["abi"],)
print("-------------------------------------------------")

while True:

    receiver = input("Type receiver address or alies that is saved in config file: ")
    message = input("Plz type the message: ")

    try:
        receiverAddress = credentials[receiver]
    except:
        receiverAddress = receiver

    nonce = w3.eth.getTransactionCount(ownerAddress)
    tx = bm_contract_instance.functions.sendLetter(
        receiverAddress, message
    ).buildTransaction(
        {"gas": 6666666, "gasPrice": w3.toWei("1", "gwei"), "nonce": nonce,}
    )

    signed_txn = w3.eth.account.sign_transaction(tx, private_key=ownerPrivateKey)
    tx_hash = w3.eth.sendRawTransaction(signed_txn.rawTransaction)
    receipt = w3.eth.waitForTransactionReceipt(tx_hash)

    print("Message sent")
    print("-------------------------------------------------")
