### READ MESSAGES AND PRINT OUT ###

from web3 import Web3
import requests
import json
import codecs
import time
import winsound

w3 = Web3(Web3.WebsocketProvider("ws://127.0.0.1:8545", websocket_timeout=200))

print("-------------------------------------------------")
print("Extracting owner, contract and receiver related info")

with open("blockchainmail_credentials.json", "r") as json_data:
    credentials = json.load(json_data)

## for dev purpose
answer = input("Are you owner? (yes or no) ")

if answer == "yes":
    ownerAddress = credentials["ownerAddress"]
    ownerPrivateKey = credentials["ownerPrivateKey"]
else:
    ownerAddress = credentials["friendAddress"]
    ownerPrivateKey = credentials["friendPrivateKey"]

bmAddress = credentials["BMAddress"]

with open("build/contracts/BlockchainMail.json", "r") as outfile:
    bm_json = json.load(outfile)

bm_contract_instance = w3.eth.contract(address=bmAddress, abi=bm_json["abi"],)

print("-------------------------------------------------")

## get events
blockNumberOld = 0
while True:

    blockNumber = w3.eth.blockNumber
    if blockNumber != blockNumberOld:
        events_new = bm_contract_instance.events.MailTransfer.createFilter(
            fromBlock=blockNumber
        ).get_all_entries()
        blockNumberOld = blockNumber
        for event in events_new:
            if event["args"]["receiverAddress"] == ownerAddress:

                print("-------------------------------------------------")
                print("*****************RECEIVED MAIL*****************")
                ## when there is event about receive letter
                frequency = 2500
                duration = 500
                winsound.Beep(frequency, duration)

                senderAddress = event["args"]["senderAddress"]
                print("Sender")
                print(senderAddress)

                receiverAddress = event["args"]["receiverAddress"]
                # print("Receiver")
                # print(receiverAddress)

                mail = bm_contract_instance.functions.receiveLatestLetter(
                    senderAddress
                ).call({"from": receiverAddress})
                print(mail)
                print("-------------------------------------------------")
