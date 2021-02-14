pragma solidity >=0.5.0 <=0.6.2;

import "OpenZeppelin/openzeppelin-contracts@3.0.0/contracts/access/Ownable.sol";
// import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v3.3.0/contracts/access/Ownable.sol";
contract BlockchainMailV3 is Ownable {

  // function viewBlockNumber() public view returns (uint){
  //   return block.number;
  // }

  BlockchainMailPool public blockchainMailPool;

  /* 1x1 mail data */
  struct ReceivedMail {
      address senderAddress;
      mapping(address => string) mail;
      mapping(address => uint) block;
  }
  mapping (address => ReceivedMail) postBox;
  event MailTransfer(address senderAddress, address receiverAddress, uint blockNumber);

  /* pool mail data */
  struct Pool {
      address poolAddress;
  }
  mapping (address => Pool) poolInfo;

  /* struct PoolMail {
    mapping(address => string) mail;
  }; */
  /* struct ReceivedPoolMail {
      BlockMail blockMail;
  } */
  /* mapping (uint => PoolMail) poolPostBox; */
  /* mapping (address => ReceivedPoolMail) poolPostBox; */
  /* event PoolMailTransfer(address poolAddress); */

  // so far only 3 people are allowed
  // create pool for getting all messages
  function createPool(address receiverAddress2, address receiverAddress3) public returns (bool){

    blockchainMailPool = new BlockchainMailPool(msg.sender,
                                                receiverAddress2,
                                                receiverAddress3);

    poolInfo[msg.sender].poolAddress = blockchainMailPool;
    poolInfo[receiverAddress2].poolAddress = blockchainMailPool;
    poolInfo[receiverAddress3].poolAddress = blockchainMailPool;
  }

  /* view pool address */
  function viewPoolAddress() public view returns (address){
    return poolInfo[msg.sender].poolAddress;
  }

  function sendPoolLetter(address poolAddress, string memory _mail) public returns (bool) {
    BlockchainMailPoolInstance(poolAddress).sendPoolLetter(msg.sender, _mail);
    /* poolPostBox[block.number].mail[msg.sender] = _mail;
    emit PoolMailTransfer(poolAddress); */
    return true;
  }

  function receiveLatestPoolLetter(address poolAddress, uint blockNumber) public view returns (string memory){
    return BlockchainMailPoolInstance(poolAddress).receiveLatestPoolLetter(msg.sender, blockNumber);
    /* return postBox[msg.sender].mail[senderAddress]; */
    /* return true; */
  }

  // 1:1 mail exchange
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

  // function letterBlock(address senderAddress) public view returns (uint){
  //   return postBox[msg.sender].block[senderAddress];
  // }

	function destroy() public onlyOwner {
	    selfdestruct(msg.sender);
	}
}
