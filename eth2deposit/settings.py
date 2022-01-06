from typing import Dict, NamedTuple
from os import environ


DEPOSIT_CLI_VERSION = '1.2.0'


class BaseChainSetting(NamedTuple):
    ETH2_NETWORK_NAME: str
    GENESIS_FORK_VERSION: bytes


#MAINNET = 'mainnet'
#PYRMONT = 'pyrmont'
#PRATER = 'prater'
GNOSIS_TESTNET = 'gnosis-testnet'
GNOSIS = 'gnosis'
TEST = 'test'


# Eth2 Mainnet setting
MainnetSetting = BaseChainSetting(ETH2_NETWORK_NAME=MAINNET, GENESIS_FORK_VERSION=bytes.fromhex('00000000'))
# Eth2 pre-launch testnet (spec v1.0.0)
PyrmontSetting = BaseChainSetting(ETH2_NETWORK_NAME=PYRMONT, GENESIS_FORK_VERSION=bytes.fromhex('00002009'))
# Eth2 testnet (spec v1.0.1)
#PraterSetting = BaseChainSetting(ETH2_NETWORK_NAME=PRATER, GENESIS_FORK_VERSION=bytes.fromhex('00001020'))

# Gnosis Beacon Chain testnet setting
GnosisTestnetSetting = BaseChainSetting(ETH2_NETWORK_NAME=GNOSIS_TESTNET, GENESIS_FORK_VERSION=bytes.fromhex('00006464'))
# Gnosis Beacon Chain setting
GnosisSetting = BaseChainSetting(ETH2_NETWORK_NAME=GNOSIS, GENESIS_FORK_VERSION=bytes.fromhex('00000064'))
TestSetting = BaseChainSetting(ETH2_NETWORK_NAME=TEST, GENESIS_FORK_VERSION=bytes.fromhex(environ.get('GENESIS_FORK_VERSION', '12345678')))


ALL_CHAINS: Dict[str, BaseChainSetting] = {
    MAINNET: MainnetSetting,
    PYRMONT: PyrmontSetting,
    PRATER: PraterSetting,
    GNOSIS_TESTNET: GnosisTestnetSetting,
    GNOSIS: GnosisSetting,
    TEST: TestSetting,
}


def get_chain_setting(chain_name: str = GNOSIS) -> BaseChainSetting:
    return ALL_CHAINS[chain_name]
