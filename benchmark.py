#!/usr/bin/env python3


# generate a random address by ethereum utils
# timeit: 1000 -> 4.9s, 74/s
def generate_eth_address_by_sha3():
    import os
    from ethereum import utils
    privKey = utils.sha3(os.urandom(4096))
    rawAddress = utils.privtoaddr(privKey)
    accAddress = utils.checksum_encode(rawAddress)
    return privKey, accAddress


# ⚡️ FASTEST:generate eth address by sha3
# timeit: 1000 -> 0.06s, 15000/s
# pip3 install coincurve,pysha3
def generate_eth_address_by_keccak():
    from secrets import token_bytes
    from coincurve import PublicKey
    from sha3 import keccak_256
    private_key = keccak_256(token_bytes(32)).digest()
    public_key = PublicKey.from_valid_secret(private_key).format(compressed=False)[1:]
    addr = keccak_256(public_key).digest()[-20:]
    return private_key.hex(), addr.hex()


# pip3 install web3
# timeit: 1000 -> 0.31s, 536/s
def generate_eth_address_by_eth_secrets():
    from eth_account import Account
    import secrets
    private_key = secrets.token_hex(32)
    acct = Account.from_key(private_key)
    return private_key, acct.address



if __name__ == '__main__':


    import timeit
    t1 = timeit.timeit(
        stmt="generate_eth_address_by_sha3()",
        setup="from __main__ import generate_eth_address_by_sha3",
        number=100)
    print(f'Method 1 speed: {int(1/t1*100)}/s')

    t2 = timeit.timeit(
        stmt="generate_eth_address_by_keccak()",
        setup="from __main__ import generate_eth_address_by_keccak",
        number=100)
    print(f'Method 2 speed: {int(1/t2*100)}/s')

    t3 = timeit.timeit(
        stmt="generate_eth_address_by_eth_secrets()",
        setup="from __main__ import generate_eth_address_by_eth_secrets",
        number=100)
    print(f'Method 3 speed: {int(1/t3*100)}/s')
