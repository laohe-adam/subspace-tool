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
    # address of subspace team
    get_balance('st9yjt9zGqrLgbgkhcqDgusQjoyuYLX2p5SBDP6Hj8D3sUAzn')
