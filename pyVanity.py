# @Name: pyVanity
# @Author: mTesla.eth
# A really fast vanity ethereum address generator

from time import sleep
from secrets import token_bytes
from coincurve import PublicKey
from sha3 import keccak_256
from ethereum import utils


# ⚡️ FASTEST way to generate eth address by sha3
# timeit: 1000 -> 0.06s
def generate_eth_address_by_keccak():
    private_key = keccak_256(token_bytes(32)).digest()
    public_key = PublicKey.from_valid_secret(private_key).format(compressed=False)[1:]
    addr = keccak_256(public_key).digest()[-20:]
    return private_key.hex(), addr.hex()


# generate specific eth address with prefix and/or suffix
def generate_vanity_address(prefix='cafe', suffix=''):
    while True:
        # get a random address
        privKey, accAddress = generate_eth_address_by_keccak()

        if accAddress.startswith(prefix) and accAddress.endswith(suffix):
            checksum_address = utils.checksum_encode(accAddress) # convert to checksum address
            print("✅ Vanity address: {}".format(checksum_address))
            print("🔰 Private Key: {} \n\n".format(privKey))
            # uncomment below to generate ONLY one address, otherwise I will never stop
            # break
    return




def main():



    prefix = input(
        "\n🤖️ Hi, I can generate the vanity ethereum address for you. Please tell me what's the prefix(less than 5 will be fast, Press Enter to skip the prefix part): "
    )

    suffix = input(
        "\n🙂 Okay, Now tell me the suffix of the address you want(Press Enter to skip the prefix part): "
    )

    if (not prefix) and (not suffix):
        sleep(1)
        print(
            '\n🤔 Seems like you tell me nothing, so let me generate some random looks-rare ethereum address for you: '
        )

        # default prefix
        prefix = '8888'


    try:
        print("\n🔭 Hang one, I'm searching the vanity ethereum address for you, type Ctrl+C to stop...\n")
        sleep(0.5)
        generate_vanity_address(prefix, suffix)
    except KeyboardInterrupt:
        print('\n😲 You called for stop, good luck next time.')


if __name__=='__main__':
    main()