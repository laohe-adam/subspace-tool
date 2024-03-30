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
    # transer()
