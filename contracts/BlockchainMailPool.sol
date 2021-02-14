pragma solidity >=0.5.0 <=0.6.2;

import "OpenZeppelin/openzeppelin-contracts@3.0.0/contracts/access/Ownable.sol";
// import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v3.3.0/contracts/access/Ownable.sol";

contract BlockchainMailPool is Ownable {

  address receiverAddress1;
  address receiverAddress2;
  address receiverAddress3;

  constructor(address _receiverAddress1;
              address _receiverAddress2;
              address _receiverAddress3) public {
    receiverAddress1 = _receiverAddress1;
    receiverAddress2 = _receiverAddress2;
    receiverAddress3 = _receiverAddress3;
   }

  struct PoolReceivedMail {
      mapping(address => string) mail;
  }

  // for each block pool will separately save messages
  /* one mail per sender */

  mapping (uint => PoolReceivedMail) poolPostBox;
  event PoolMailTransfer(address senderAddress, uint blockNumber);

  // no need receiver address since every mail comes into the pool
  function sendPoolLetter(address senderAddress, string memory _mail) public returns (bool) {
    poolPostBox[block.number].mail[senderAddress] = _mail;

    // emit event about new mails
    emit PoolMailTransfer(senderAddress, block.number);
    return true;
  }

  function receivePoolLetter(address senderAddress, uint blockNumber) public view returns (string memory){
    return poolPostBox[blockNumber].mail[msg.sender];
  }

	function destroy() public onlyOwner {
	    selfdestruct(msg.sender);
	}
}
