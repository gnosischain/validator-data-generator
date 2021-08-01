from typing import Dict, NamedTuple
from os import environ


DEPOSIT_CLI_VERSION = '2.0.0'


class BaseChainSetting(NamedTuple):
    NETWORK_NAME: str
    GENESIS_FORK_VERSION: bytes


MAINNET = 'mainnet'
PRATER = 'prater'
KINTSUGI = 'kintsugi'
KILN = 'kiln'
STAKE = 'stake'
TEST = 'test'


# Mainnet setting
MainnetSetting = BaseChainSetting(NETWORK_NAME=MAINNET, GENESIS_FORK_VERSION=bytes.fromhex('00000000'))
# Testnet (spec v1.0.1)
PraterSetting = BaseChainSetting(NETWORK_NAME=PRATER, GENESIS_FORK_VERSION=bytes.fromhex('00001020'))
# Merge Testnet (spec v1.1.4)
KintsugiSetting = BaseChainSetting(NETWORK_NAME=KINTSUGI, GENESIS_FORK_VERSION=bytes.fromhex('60000069'))
# Merge Testnet (spec v1.1.9)
KilnSetting = BaseChainSetting(NETWORK_NAME=KILN, GENESIS_FORK_VERSION=bytes.fromhex('70000069'))

StakeSetting = BaseChainSetting(ETH2_NETWORK_NAME=STAKE, GENESIS_FORK_VERSION=bytes.fromhex('00006464'))
TestSetting = BaseChainSetting(NETWORK_NAME=TEST, GENESIS_FORK_VERSION=bytes.fromhex(environ.get('GENESIS_FORK_VERSION', '12345678')))


ALL_CHAINS: Dict[str, BaseChainSetting] = {
    MAINNET: MainnetSetting,
    PRATER: PraterSetting,
    KINTSUGI: KintsugiSetting,
    KILN: KilnSetting,
    STAKE: StakeSetting,
    TEST: TestSetting,
}


def get_chain_setting(chain_name: str = MAINNET) -> BaseChainSetting:
    return ALL_CHAINS[chain_name]
