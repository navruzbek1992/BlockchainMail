# Blockchain Mail

BM is live on ropsten (https://ropsten.etherscan.io/address/0x176A3014B7D16b5684A0B8a116d68fA28099Cd92) and on mumbai (https://explorer-mumbai.maticvigil.com/address/0x70a6fd6AB3ed7730C83D2Ab8C3e6F77AB507bB05/transactions).

## For developers

Works only with ropsten deployed contract.

### Steps

- Download and unzip repo folder
- In credentials file include your address and key for signing and sending message
- In credentials file include your friends address (Currently my address is included. Feel free to replace with other peoples address)
- In credentials include infura project ID
- In CMD (or anaconda prompt) run `pip install -r requirements.txt`
- In a seperate CMD (or anaconda prompt) run `python bm_receiver.py` 
- In a seperate CMD (or anaconda prompt) run `python bm_sender.py`

Keep running receiver and sender in separate CMD.
You get message in receiver win and send message in sender win.
Sender win asks friend address. You can paste friend address but if you want to keep things comfy, just type "friendAddress".

## GUI 

Works only with ropsten deployed contract.

### Steps

- Download and unzip repo folder
- Have a ready infura link 
- In CMD (or anaconda prompt) run `pip install -r requirements.txt`
- In a seperate CMD (or anaconda prompt) run `python bmgui.py`


Enjoy chatting with friends.

In the future, contract will be extended to handle group chats. So far it is 1:1 chat.
Also messages are not encrypted. To keep things safe it is for simple chat only.
In the future contract will encrypt messages. 

## Executable file

Executable files are in blockchainmail.zip folder. Works only with mumbai deployed contract.

### Steps
- Download and unzip them. 
- No need python installation or infura link is required. 
- Only thing is to get matic testnet tokens (https://faucet.matic.network/).
- Open blockchain.exe file in unzipped folder. GUI will appear. 
- Enter sender (your), receiver (friend) and private key info. And press connect.
- After connection receive mail or send mail.
