from dataclasses import dataclass
from typing import Optional, Any


@dataclass
class TokenHoldingSecurityData:
    name: str = None
    ticker: str = None
    ca: str = None
    amount: float = None
    price: float = None
    total_value: float = None

    anti_whale_modifiable: bool = None
    buy_tax: float = None
    can_take_back_ownership: bool = None
    cannot_buy: bool = None
    cannot_sell_all: bool = None
    creator_address: str = None
    creator_balance: float = None
    creator_percent: float = None
    external_call: bool = None
    fake_token: Optional[bool] = None
    hidden_owner: bool = None
    holder_count: float = None
    honeypot_with_same_creator: bool = None
    is_airdrop_scam: Optional[bool] = None
    is_anti_whale: bool = None
    is_blacklisted: bool = None
    is_honeypot: bool = None
    is_in_dex: bool = None
    is_mintable: bool = None
    is_open_source: bool = None
    is_proxy: bool = None
    is_true_token: Optional[bool] = None
    is_whitelisted: bool = None
    lp_holder_count: float = None
    lp_total_supply: float = None
    note: Optional[str] = None
    other_potential_risks: Optional[str] = None
    owner_address: str = None
    owner_balance: float = None
    owner_change_balance: float = None
    owner_percent: float = None
    personal_slippage_modifiable: bool = None
    selfdestruct: bool = None
    sell_tax: float = None
    slippage_modifiable: bool = None
    token_name: str = None
    token_symbol: str = None
    total_supply: float = None
    trading_cooldown: bool = None
    transfer_pausable: bool = None
    trust_list: bool = None

    def append_goplus_security_data(self, data: Any) -> None:
        def str_to_bool(value: Optional[bool]) -> Optional[bool]:
            try:
                return value == "1"
            except Exception as e:
                print(e)
            return None

        def to_float(value: Optional[float]) -> Optional[float]:
            try:
                if value is not None:
                    return float(value)
            except Exception as e:
                print(e)
            return None

        self.anti_whale_modifiable = str_to_bool(data.anti_whale_modifiable)
        self.buy_tax = to_float(data.buy_tax)
        self.can_take_back_ownership = str_to_bool(data.can_take_back_ownership)
        self.cannot_buy = str_to_bool(data.cannot_buy)
        self.cannot_sell_all = str_to_bool(data.cannot_sell_all)
        self.creator_address = data.creator_address
        self.creator_balance = to_float(data.creator_balance)
        self.creator_percent = to_float(data.creator_percent)
        self.external_call = str_to_bool(data.external_call)
        self.fake_token = str_to_bool(data.fake_token) if data.fake_token is not None else None
        self.hidden_owner = str_to_bool(data.hidden_owner)
        self.holder_count = to_float(data.holder_count)
        self.honeypot_with_same_creator = str_to_bool(data.honeypot_with_same_creator)
        self.is_airdrop_scam = str_to_bool(data.is_airdrop_scam) if data.is_airdrop_scam is not None else None
        self.is_anti_whale = str_to_bool(data.is_anti_whale)
        self.is_blacklisted = str_to_bool(data.is_blacklisted)
        self.is_honeypot = str_to_bool(data.is_honeypot)
        self.is_in_dex = str_to_bool(data.is_in_dex)
        self.is_mintable = str_to_bool(data.is_mintable)
        self.is_open_source = str_to_bool(data.is_open_source)
        self.is_proxy = str_to_bool(data.is_proxy)
        self.is_true_token = str_to_bool(data.is_true_token) if data.is_true_token is not None else None
        self.is_whitelisted = str_to_bool(data.is_whitelisted)
        self.lp_holder_count = to_float(data.lp_holder_count)
        self.lp_total_supply = to_float(data.lp_total_supply)
        self.note = data.note
        self.other_potential_risks = data.other_potential_risks
        self.owner_address = data.owner_address
        self.owner_balance = to_float(data.owner_balance)
        self.owner_change_balance = to_float(data.owner_change_balance)
        self.owner_percent = to_float(data.owner_percent)
        self.personal_slippage_modifiable = str_to_bool(data.personal_slippage_modifiable)
        self.selfdestruct = str_to_bool(data.selfdestruct)
        self.sell_tax = to_float(data.sell_tax)
        self.slippage_modifiable = str_to_bool(data.slippage_modifiable)
        self.token_name = data.token_name
        self.token_symbol = data.token_symbol
        self.total_supply = to_float(data.total_supply)
        self.trading_cooldown = str_to_bool(data.trading_cooldown)
        self.transfer_pausable = str_to_bool(data.transfer_pausable)
        self.trust_list = str_to_bool(data.trust_list)