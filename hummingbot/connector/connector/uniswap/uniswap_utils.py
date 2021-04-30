CENTRALIZED = False
EXAMPLE_PAIR = "WETH-DAI"
DEFAULT_FEES = [0., 0.]

USE_EVM = 'ethereum'
FEE_TYPE = "FlatFee"
FEE_TOKEN = "ETH"

USE_ETH_GAS_LOOKUP = True

# TODO: Can remove or add to docs as an example
OTHER_DOMAINS = ["uniswap_xdai"]
OTHER_DOMAINS_PARAMETER = {"uniswap_xdai": "xdai"}
OTHER_DOMAINS_EXAMPLE_PAIR = {"uniswap_xdai": "WXDAI-WETH"}
OTHER_DOMAINS_DEFAULT_FEES = {"uniswap_xdai": [0., 0.]}
OTHER_DOMAINS_USE_EVM = {"uniswap_xdai": "evm"}
OTHER_DOMAINS_FEE_TYPE = {"uniswap_xdai": "FlatFee"}
OTHER_DOMAINS_FEE_TOKEN = {"uniswap_xdai": ""}  # TODO ****
OTHER_DOMAINS_USE_ETH_GAS_LOOKUP = {"uniswap_xdai": False}
