from tkinter import *
import time
from web3 import Web3
import requests
import json
import codecs


def connect():
    infuraLinkEntryInfo = infuraLinkEntry.get()
    yourAddressEntryInfo = yourAddressEntry.get()
    friendAddressEntryInfo = friendAddressEntry.get()

    button.configure(state="disabled")

    global params
    global ownerAddress
    global ownerPrivateKey
    global yourFriendAddress
    global w3
    global bm_contract_instance
    global bmAddress

    bmAddress = "0x176A3014B7D16b5684A0B8a116d68fA28099Cd92"
    params = [infuraLinkEntryInfo, yourAddressEntryInfo, friendAddressEntryInfo]
    ownerAddress = yourAddressEntryInfo
    ownerPrivateKey = yourPrivateKey
    yourFriendAddress = friendAddressEntryInfo

    w3 = Web3(Web3.WebsocketProvider(infuraLinkEntryInfo, websocket_timeout=200))

    with open("blockchain_mail/build/contracts/BlockchainMail.json", "r") as outfile:
        bm_json = json.load(outfile)
    bm_contract_instance = w3.eth.contract(address=bmAddress, abi=bm_json["abi"],)

    if w3.isConnected():
        R.insert(END, "---------")
        R.insert(END, "CONNECTED")
        R.insert(END, "---------")


def receive():

    R.insert(END, "****CHECKING****")

    count = 10
    while count < 10:
        events_new = bm_contract_instance.events.MailTransfer.createFilter(
            fromBlock="latest"
        ).get_all_entries()
        for event in events_new:
            if event["args"]["receiverAddress"] == ownerAddress:

                senderAddress = event["args"]["senderAddress"]
                receiverAddress = event["args"]["receiverAddress"]

                mail = bm_contract_instance.functions.receiveLatestLetter(
                    senderAddress
                ).call({"from": receiverAddress})

                R.insert(END, "****START**")
                R.insert(END, mail)
                R.insert(END, "**END****")
        count += 1


def send():
    w3 = Web3(Web3.WebsocketProvider(infuraLinkEntryInfo, websocket_timeout=200))
    with open("blockchain_mail/build/contracts/BlockchainMail.json", "r") as outfile:
        bm_json = json.load(outfile)
    bm_contract_instance = w3.eth.contract(address=bmAddress, abi=bm_json["abi"],)

    mail = sendMailTextEntry.get()
    nonce = w3.eth.getTransactionCount(ownerAddress)
    tx = bm_contract_instance.functions.sendLetter(
        yourFriendAddress, mail
    ).buildTransaction(
        {"gas": 6666666, "gasPrice": w3.toWei("10", "gwei"), "nonce": nonce,}
    )

    signed_txn = w3.eth.account.sign_transaction(tx, private_key=ownerPrivateKey)
    tx_hash = w3.eth.sendRawTransaction(signed_txn.rawTransaction)
    receipt = w3.eth.waitForTransactionReceipt(tx_hash)

    R.insert(END, "****SENT**START")
    R.insert(END, mail)
    R.insert(END, "**END****")


params = [0, 0, 0]
app = Tk()

app.geometry("900x500")
app.title("Blockchain Mail")

heading = Label(
    text="Blockchain Mail", fg="black", bg="skyblue", width="500", height="1", font="10"
)
heading.pack()

R = Text(app, height=30, width=30)
R.pack()
R.insert(END, "")

infura_link = Label(text="Infura link :")
your_address = Label(text="Your address :")
friend_address = Label(text="Friend address :")
send_mail_text = Label(text="Mail :")

infura_link.place(x=15, y=60)
your_address.place(x=15, y=100)
friend_address.place(x=15, y=140)
send_mail_text.place(x=15, y=400)

infuraLink = StringVar()
yourAddress = StringVar()
friendAddress = StringVar()
sendMailText = Text()

infuraLinkEntry = Entry(textvariable=infuraLink, width="50")
yourAddressEntry = Entry(textvariable=yourAddress, width="50")
friendAddressEntry = Entry(textvariable=friendAddress, width="50")
sendMailTextEntry = Entry(textvariable=sendMailText, width="50")

infuraLinkEntry.place(x=15, y=80)
yourAddressEntry.place(x=15, y=120)
friendAddressEntry.place(x=15, y=160)
sendMailTextEntry.place(x=15, y=420)

button = Button(
    app, text="Connect blockchain", command=connect, width="20", height="1", bg="grey"
)
button.place(x=15, y=200)

receive = Button(
    app, text="Receive mail", command=receive, width="10", height="1", bg="grey"
)
receive.place(x=15, y=350)

receive = Button(app, text="Send mail", command=send, width="10", height="1", bg="grey")
receive.place(x=15, y=450)


if __name__ == "__main__":
    mainloop()
