from web3 import Web3

# 连接到以太坊节点，可以使用Infura提供的节点或者本地节点
w3 = Web3(Web3.HTTPProvider('你的以太坊节点URL'))

def check_contract_deployed(address):
    # 获取指定地址的代码
    contract_code = w3.eth.getCode(address)

    # 如果代码长度大于2（"0x"），则说明合约已经部署
    if len(contract_code) > 2:
        print(f"地址 {address} 已部署合约。")
    else:
        print(f"地址 {address} 没有部署合约。")

# 替换下面的地址为你要查询的地址
address_to_check = "0xYourAddress"
check_contract_deployed(address_to_check)
