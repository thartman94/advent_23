from functools import reduce

MAX_VALUES = {"red": 12, "green": 13, "blue": 14}


def is_possible(game: str) -> bool:
    rounds = game.split(": ")[-1].split("; ")
    vals = [rnd.split(", ") for rnd in rounds]
    print(rounds)
    print(vals)
    local_max = {"red": 0, "green": 0, "blue": 0}
    for v in vals:
        print(v)
        [x, color] = v.split(" ")
        local_max[color] = max(local_max[color], x)

    for m in local_max.keys():
        if local_max[m] > MAX_VALUES[m]:
            return False

    return True


def answer_1() -> int:
    res = 0
    with open("data.txt") as data:
        for i, game in enumerate(data):
            res += i + 1 if is_possible(game) else 0
    return res


# def answer_2() -> int:
#     res = 0
#     with open("data.txt") as data:
#         for line in data:
#             res += int(find_digit(line) + find_digit(line, reversed=True))
#     return res


if __name__ == "__main__":
    print("===================\n")
    print(f"Answer 1: {answer_1()}")
    # print(f"Answer 2: {answer_2()}")
