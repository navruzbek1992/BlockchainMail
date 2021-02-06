# Blockchain Mail

BM is live in ropsten. Here is the address 0x176A3014B7D16b5684A0B8a116d68fA28099Cd92.

## Steps

- Download and unzip repo folder
- In credentials file include your address and key for signing and sending message
- In credentials file include your friends address (Currently my address is included. Feel free to replace with other peoples address)
- In credentials include infura project ID
- In CMD run `pip install -r requirements.txt`
- In a seperate CMD run `python bm_receiver.py`
- In a seperate CMD run `python bm_sender.py`

Keep running receiver and sender in separate CMD.
You get message in receiver win and send message in sender win.
Sender win asks friend address. You can paste friend address but if you want to keep things comfy, just type "friendAddress".

Enjoy chatting with friends.
