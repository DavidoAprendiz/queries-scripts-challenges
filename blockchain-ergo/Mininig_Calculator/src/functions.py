# Calculations

def kw_per_hours(_watts_h: float, _hours: float) -> float:
    return round((_watts_h / 1000) * _hours, 2)


def daily_block_rewards(_block_reward: float) -> float:
    return _block_reward * 720


def daily_block_rewards_in_value(_block_reward: float, _price: float) -> float:
    return round(daily_block_rewards(_block_reward) * _price, 2)


def daily_spent_in_value(_watts_h: float, _hours: float, _kw_h_price: float) -> float:
    return round(kw_per_hours(_watts_h, _hours) * _kw_h_price, 2)


def daily_block_rewards_in_value_for_hashrate(_block_reward: float, _price: float, _network_hashrate: float) -> float:
    return daily_block_rewards_in_value(_block_reward, _price) / _network_hashrate
