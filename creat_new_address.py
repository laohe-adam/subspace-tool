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
