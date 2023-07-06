def map_to_dict(header: int, lines: list[str]):
    sorted = {}
    for idl, line in enumerate(lines):
        if idl == 0:
            continue

        values = line.strip().split(",")
        header_value = values[header]

        sorted[header_value] = values

    return sorted


def map_to_dict_distinct(header: int, lines: list[str]):
    sorted = {}
    for idl, line in enumerate(lines):
        if idl == 0:
            continue

        values = line.strip().split(",")
        header_value = values[header]

        if header_value not in sorted:
            sorted[header_value] = []

        sorted[header_value].append(values)

    return sorted


def get_votes_per_legislator(__d_vote_results: dict):
    data = {}

    def get_votes_ids_per_vote_condition(__votes: list[str], condition: int):
        return list(
            map(
                lambda x: int(x[2]),
                filter(
                    lambda x: int(x[3]) == condition,
                    __votes,
                ),
            )
        )

    for key, value in __d_vote_results.items():
        yea = get_votes_ids_per_vote_condition(value, 2)
        nay = get_votes_ids_per_vote_condition(value, 1)
        data[key] = [yea, nay]
    return data


def get_bills_votes_per_legislator(__d_vote_results: dict, __d_votes: dict):
    data = {}
    for key, value in __d_votes.items():
        header_value = value[1]
        data[header_value] = [[], []]
        for key1, value1 in __d_vote_results.items():
            if int(key) in value1[0]:
                data[header_value][0].append(key1)
            if int(key) in value1[1]:
                data[header_value][1].append(key1)
    return data


def buildAnwser1(__votes_per_legislator: dict, __d_legislators: dict):
    def get_values(kv):
        id = kv[0]
        name = __d_legislators[id][1]
        num_supported_bills = len(kv[1][0])
        num_opposed_bills = len(kv[1][1])
        return [id, name, num_supported_bills, num_opposed_bills]

    headers = ["id", "name", "num_supported_bills", "num_opposed_bills"]
    data = [
        headers,
        *list(
            map(
                lambda kv: get_values(kv),
                __votes_per_legislator.items(),
            )
        ),
    ]
    write_csv_from_list(data, "legislators-support-oppose-count.csv")


def buildAnwser2(
    __bills_votes_per_legislator: dict, __d_bills: dict, __d_legislators: dict
):
    def get_values(kv):
        id = kv[0]

        d_bill = __d_bills[id]

        title = __d_bills[id][1]
        supporter_count = len(kv[1][0])
        opposer_count = len(kv[1][1])
        primary_sponsor = "not_found"

        if d_bill[2] in __d_legislators:
            primary_sponsor = __d_legislators[d_bill[2]][1]
        return [id, title, supporter_count, opposer_count, primary_sponsor]

    headers = ["id", "title", "supporter_count", "opposer_count", "primary_sponsor"]
    data = [
        headers,
        *list(
            map(
                lambda kv: get_values(kv),
                __bills_votes_per_legislator.items(),
            )
        ),
    ]
    write_csv_from_list(data, "bills.csv")


def write_csv_from_list(data: list, filename: str):
    lines = list(
        map(
            lambda value: ",".join(
                map(
                    lambda v: str(v),
                    value,
                )
            ),
            data,
        )
    )

    with open(filename, "w") as f:
        f.write("\n".join(lines))


l_bills = open("./data/bills.csv", "r").readlines()
l_legislators = open("./data/legislators.csv", "r").readlines()
l_vote_results = open("./data/vote_results.csv", "r").readlines()
l_votes = open("./data/votes.csv", "r").readlines()

d_legislators = map_to_dict(0, l_legislators)  # per id
d_bills = map_to_dict(0, l_bills)  # per legislator id
d_vote_results = map_to_dict_distinct(1, l_vote_results)  # per legislator id
d_votes = map_to_dict(0, l_votes)  # per bill id

votes_per_legislator = get_votes_per_legislator(d_vote_results)
bills_votes_per_legislator = get_bills_votes_per_legislator(
    votes_per_legislator, d_votes
)

buildAnwser1(votes_per_legislator, d_legislators)
buildAnwser2(bills_votes_per_legislator, d_bills, d_legislators)
