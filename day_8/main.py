from functools import reduce
import math

MAX_VALUES = {"red": 12, "green": 13, "blue": 14}


def answer_1() -> int:
    directions = ""
    vals = {}
    cur = "AAA"
    res = 0
    with open("data.txt") as data:
        for i, line in enumerate(data):
            if i == 0:
                directions = line
                continue
            if i == 1:
                continue

            v = line.strip().replace("(", "").replace(")", "").split(" = ")
            vv = v[1].split(", ")
            vals[v[0]] = [
                vv[0],
                vv[1],
            ]

    i = 0
    while cur != "ZZZ":
        d = int(directions[i] == "R")
        cur = vals[cur][d]
        i = (i + 1) % (len(directions) - 1)
        res += 1

    return res


def run_the_glove(start, directions, vals):
    cur = start
    res, i = 0, 0
    while not cur.endswith("Z"):
        d = int(directions[i] == "R")
        cur = vals[cur][d]
        i = (i + 1) % (len(directions) - 1)
        res += 1

    return res


def answer_2() -> int:
    directions = ""
    vals = {}
    res = 0
    with open("data.txt") as data:
        for i, line in enumerate(data):
            if i == 0:
                directions = line
                continue
            if i == 1:
                continue

            v = line.strip().replace("(", "").replace(")", "").split(" = ")
            vv = v[1].split(", ")
            vals[v[0]] = [
                vv[0],
                vv[1],
            ]

    i = 0
    cur = [v for v in vals.keys() if v.endswith("A")]

    return math.lcm(*[run_the_glove(start, directions, vals) for start in cur])


if __name__ == "__main__":
    print("===================\n")
    print(f"Answer 1: {answer_1()}")
    print(f"Answer 2: {answer_2()}")
