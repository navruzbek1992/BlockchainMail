pragma solidity >=0.5.0 <=0.6.2; //used060

import "OpenZeppelin/openzeppelin-contracts@3.0.0/contracts/access/Ownable.sol";

contract BlockchainMail is Ownable {

  function viewBlockNumber() public view returns (uint){
    return block.number;
  }

  struct ReceivedMail {
      address senderAddress;
      mapping(address => string) mail;
      mapping(address => uint) block;
  }
  mapping (address => ReceivedMail) postBox;
  event MailTransfer(address senderAddress, address receiverAddress, uint blockNumber);

  function sendLetter(address receiverAddress, string memory _mail) public returns (bool) {
    postBox[receiverAddress].mail[msg.sender] = _mail;
    postBox[receiverAddress].block[msg.sender] = block.number;
    postBox[receiverAddress].senderAddress = msg.sender;

    emit MailTransfer(msg.sender, receiverAddress, block.number);
    return true;
  }

  function receiveLatestLetter(address senderAddress) public view returns (string memory){
    return postBox[msg.sender].mail[senderAddress];
  }

  function letterBlock(address senderAddress) public view returns (uint){
    return postBox[msg.sender].block[senderAddress];
  }

	function destroy() public onlyOwner {
	    selfdestruct(msg.sender);
	}
}
