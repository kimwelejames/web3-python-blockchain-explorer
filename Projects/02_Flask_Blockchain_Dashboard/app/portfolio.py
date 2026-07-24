def calculate_portfolio_stats(portfolio, eth_balance, eth_price):

    eth_balance = float(eth_balance or 0)
    eth_price = float(eth_price or 0)

    portfolio_value = round(eth_balance * eth_price, 2)

    token_count = len(portfolio)

    active_tokens = 0
    total_token_balance = 0

    for token in portfolio:
        balance = float(token.get("balance", 0))

        if balance > 0:
            active_tokens += 1

        total_token_balance += balance

    return {
        "portfolio_value": portfolio_value,
        "token_count": token_count,
        "active_tokens": active_tokens,
        "total_token_balance": round(total_token_balance, 4)
    }