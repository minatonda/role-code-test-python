lines = open("./dataset.csv", "r").readlines()


def get_accounts_executed_at_least_transactions(a: dict, b: int):
    accounts = []
    for key, value in a.items():
        if len(value) >= b:
            accounts.append(key)

    return accounts


def get_accounts_avg(a: dict):
    avg = {}
    for key, value in a.items():
        transaction_values = list(
            map(
                lambda x: int(x[2]),
                value,
            )
        )
        avg[key] = sum(transaction_values) / len(transaction_values)

    return avg


def get_accounts_highest(a: dict, b: int = 0):
    c = sorted(a.items(), key=lambda item: item[1])
    c.reverse()
    return list(c)[b]


def get_unique_buy_sell_combinations(a: dict):
    buy_sells = []
    for key, value in a.items():
        for v1 in value:
            buy_sells.append("{}-{}".format(key, v1[0]))

    buy_sells = list(set(buy_sells))
    buy_sells.sort()
    return buy_sells


sorted_per_account = {}
sorted_per_buy_sell_currency = {}

for idl, line in enumerate(lines):
    if idl == 0:
        continue

    values = line.strip().split(",")

    if values[3] not in sorted_per_account:
        sorted_per_account[values[3]] = []

    if values[0] not in sorted_per_buy_sell_currency:
        sorted_per_buy_sell_currency[values[0]] = []

    sorted_per_account[values[3]].append(values[0:3])
    sorted_per_buy_sell_currency[values[0]].append(values[1:4])


accounts_at_least_500_transactions = get_accounts_executed_at_least_transactions(
    sorted_per_account, 500
)

unique_buy_sell_combinations = get_unique_buy_sell_combinations(
    sorted_per_buy_sell_currency
)

accounts_avg = get_accounts_avg(sorted_per_account)
accounts_highest_avg = get_accounts_highest(accounts_avg,2)

print(
    "number of accounts with at least 500 transactions : {}".format(
        len(accounts_at_least_500_transactions)
    )
)
print(
    "number of unique by sell combinations : {}".format(
        len(unique_buy_sell_combinations)
    )
)

print("account that has the 3th highest average ammount: {} - {}".format(*accounts_highest_avg))
