from functools import reduce


def get_next(val, m):
    for n in m:
        if val >= n["low"] and val <= n["hi"]:
            return val + n["inc"]
    return val


def answer_1() -> int:
    res = float("inf")
    seeds = []
    maps = []
    j = -1
    skip = False
    with open("data.txt") as data:
        for i, line in enumerate(data):
            if i == 0:
                seeds = [int(c) for c in line.strip().split(": ")[1].split(" ")]
                continue

            if not line.strip():
                j += 1
                maps.append([])
                skip = True
                continue

            if skip:
                skip = False
                continue

            x = [int(c) for c in line.strip().split(" ")]
            maps[j].append({"low": x[1], "hi": x[1] + x[2] - 1, "inc": x[0] - x[1]})

    for seed in seeds:
        nxt = seed
        for m in maps:
            nxt = get_next(nxt, m)
        res = min(nxt, res)

    return res


def answer_2() -> int:
    res = float("inf")
    seeds = []
    maps = []
    j = -1
    skip = False
    with open("data.txt") as data:
        for i, line in enumerate(data):
            if i == 0:
                fake_seeds = [int(c) for c in line.strip().split(": ")[1].split(" ")]
                k = 0
                while k < len(fake_seeds) - 1:
                    seeds.append({"start": fake_seeds[k], "range": fake_seeds[k + 1]})
                    k += 2
                continue

            if not line.strip():
                j += 1
                maps.append([])
                skip = True
                continue

            if skip:
                skip = False
                continue

            x = [int(c) for c in line.strip().split(" ")]
            maps[j].append({"low": x[1], "hi": x[1] + x[2] - 1, "inc": x[0] - x[1]})

    total_seeds = reduce(lambda x, y: x + y["range"], seeds, 0)

    j = 0
    for seed in seeds:
        for i in range(seed["range"]):
            nxt = seed["start"] + i
            for m in maps:
                nxt = get_next(nxt, m)
            res = min(nxt, res)
            j += 1
            if not j % 100000:
                print(f"{(j / total_seeds) * 100}%")

    return res


if __name__ == "__main__":
    print("===================\n")
    print(f"Answer 1: {answer_1()}")
    print(f"Answer 2: {answer_2()}")
