# subspace-tool 备注:中文文档在下方

## Install requie
The substrateinterface is office python SDK by polkadot 
https://polkadot.network/

```python
pip install substrateinterface
pip install csv
```



## The tool func list


## 1、creat a new address 

```python

from substrateinterface import Keypair, SubstrateInterface, keypair
import csv


def creat_new_address(creat_number: int, url: str = None,save_file_name:str = None) -> None:
    """
    :param creat_number:\number of wallet taht you want creat;
    :param url: network PRC,Default is subspace tssc3h   wss://rpc-1.gemini-3h.subspace.network/ws;
    :param save_file_name:the name of save csv
    :return:None,But the wallet will save in csv;
    """
    if url:
        substrate = SubstrateInterface(url=url)
    else:
        substrate = SubstrateInterface(url="wss://rpc-1.gemini-3h.subspace.network/ws")

    if save_file_name:
        save_file_name = save_file_name
    else:
        save_file_name = 'wallet.csv'

    def creat():

        mnemonic_ = keypair.Keypair.generate_mnemonic()

        keypair_alice = Keypair.create_from_uri(mnemonic_, ss58_format=substrate.ss58_format)

        address = keypair_alice.ss58_address
        mnemonic = keypair_alice.mnemonic

        with open(save_file_name, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([address, mnemonic])

        print(address)
        print(mnemonic)

    _ = [creat() for i in range(creat_number)]
    print(f'Number of {creat_number} is done')


if __name__ == '__main__':
    creat_new_address(1)


## 2、get adress balance

```python

from substrateinterface import SubstrateInterface


substrate = SubstrateInterface(url="wss://rpc-1.gemini-3h.subspace.network/ws")


def get_balance(wallet_address: str) -> float:
    """

    :param wallet_address:/ wallet
    :return:
    """

    try:
        result = substrate.query("System", "Account", [wallet_address])
        balance = result.value["data"]["free"] + result.value["data"]["reserved"]
        balance = round(balance / 10 ** substrate.properties.get('tokenDecimals', 0), 3)
        print(f' Balance  : {balance}  -  {wallet_address} ')
        return balance
    except:
        print(f'Erro with Get Balance,Maybe Close VPN or install and update your liabrary')


if __name__ == '__main__':
    # address of you
    get_balance('Your address')



```

## 3、tranfer your Tssc(3h) assest
```python

from substrateinterface import SubstrateInterface, Keypair
from substrateinterface.exceptions import SubstrateRequestException

def transer(mnemonic, recipient_address, transfer_amount, url=None):
    """

    :param mnemonic:
    :param recipient_address: /recpient address
    :param transfer_amount:  / amount of you want to transfer
    :param url:
    :return:
    """
    if url:
        substrate = SubstrateInterface(url=url)
    else:
        substrate = SubstrateInterface(url="wss://rpc-1.gemini-3h.subspace.network/ws")
    sender_mnemonic = mnemonic
    sender_keypair = Keypair.create_from_mnemonic(sender_mnemonic)

    recipient_address = recipient_address

    amount = transfer_amount * 10 ** 18

    call = substrate.compose_call(
        call_module="Balances",
        call_function="transfer_keep_alive",
        call_params={"dest": recipient_address, "value": f'{amount}'}
    )

    extrinsic = substrate.create_signed_extrinsic(call=call, keypair=sender_keypair)

    try:
        receipt = substrate.submit_extrinsic(extrinsic, wait_for_inclusion=True)
        print(f"Transfer successful. Extrinsic hash: {receipt.extrinsic_hash}")
        print(f"The transer link is - \n  https://subspace.subscan.io/extrinsic/{receipt.extrinsic_hash}")
    except SubstrateRequestException as e:
        print(f"Transfer failed: {e}")


if __name__ == '__main__':
    pass
    # transer('Your menonic','recipient_address','amouont of transfer')



```
# ==========================================================================================
# 中文文档
## 功能清单

## 1、创建地址
```python

from substrateinterface import Keypair, SubstrateInterface, keypair
import csv


def creat_new_address(creat_number: int, url: str = None,save_file_name:str = None) -> None:
    """
    :param creat_number:\number of wallet taht you want creat;
    :param url: network PRC,Default is subspace tssc3h   wss://rpc-1.gemini-3h.subspace.network/ws;
    :param save_file_name:the name of save csv
    :return:None,But the wallet will save in csv;
    """
    if url:
        substrate = SubstrateInterface(url=url)
    else:
        substrate = SubstrateInterface(url="wss://rpc-1.gemini-3h.subspace.network/ws")

    if save_file_name:
        save_file_name = save_file_name
    else:
        save_file_name = 'wallet.csv'

    def creat():

        mnemonic_ = keypair.Keypair.generate_mnemonic()

        keypair_alice = Keypair.create_from_uri(mnemonic_, ss58_format=substrate.ss58_format)

        address = keypair_alice.ss58_address
        mnemonic = keypair_alice.mnemonic

        with open(save_file_name, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([address, mnemonic])

        print(address)
        print(mnemonic)

    _ = [creat() for i in range(creat_number)]
    print(f'Number of {creat_number} is done')


if __name__ == '__main__':
    # 参数为需要创建多少地址
    # 可以通过save_file_name参数更改默认保存的csv文件
    creat_new_address(1)

## 2、查看余额

```python

from substrateinterface import SubstrateInterface


substrate = SubstrateInterface(url="wss://rpc-1.gemini-3h.subspace.network/ws")


def get_balance(wallet_address: str) -> float:
    """

    :param wallet_address:/ wallet
    :return:
    """

    try:
        result = substrate.query("System", "Account", [wallet_address])
        balance = result.value["data"]["free"] + result.value["data"]["reserved"]
        balance = round(balance / 10 ** substrate.properties.get('tokenDecimals', 0), 3)
        print(f' Balance  : {balance}  -  {wallet_address} ')
        return balance
    except:
        print(f'Erro with Get Balance,Maybe Close VPN or install and update your liabrary')


if __name__ == '__main__':
    # 下面的填入你的地址即可
    get_balance('Your address')


## 3、转账 tssc [3h]

```python

from substrateinterface import SubstrateInterface, Keypair
from substrateinterface.exceptions import SubstrateRequestException

def transer(mnemonic, recipient_address, transfer_amount, url=None):
    """

    :param mnemonic:
    :param recipient_address: /recpient address
    :param transfer_amount:  / amount of you want to transfer
    :param url:
    :return:
    """
    if url:
        substrate = SubstrateInterface(url=url)
    else:
        substrate = SubstrateInterface(url="wss://rpc-1.gemini-3h.subspace.network/ws")
    sender_mnemonic = mnemonic
    sender_keypair = Keypair.create_from_mnemonic(sender_mnemonic)

    recipient_address = recipient_address

    amount = transfer_amount * 10 ** 18

    call = substrate.compose_call(
        call_module="Balances",
        call_function="transfer_keep_alive",
        call_params={"dest": recipient_address, "value": f'{amount}'}
    )

    extrinsic = substrate.create_signed_extrinsic(call=call, keypair=sender_keypair)

    try:
        receipt = substrate.submit_extrinsic(extrinsic, wait_for_inclusion=True)
        print(f"Transfer successful. Extrinsic hash: {receipt.extrinsic_hash}")
        print(f"The transer link is - \n  https://subspace.subscan.io/extrinsic/{receipt.extrinsic_hash}")
    except SubstrateRequestException as e:
        print(f"Transfer failed: {e}")


if __name__ == '__main__':
    # 参数: 助记词、接受地址、转账数量
    transer('Your menonic','recipient_address','amouont of transfer')

```
