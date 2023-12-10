from functools import reduce

DIGITS = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

DIGITS_REMIX = {
    "eno": "1",
    "owt": "2",
    "eerht": "3",
    "ruof": "4",
    "evif": "5",
    "xis": "6",
    "neves": "7",
    "thgie": "8",
    "enin": "9",
}


def find_digit(line: str, reversed: bool = False) -> str:
    digits, line = (DIGITS_REMIX, line[::-1]) if reversed else (DIGITS, line)
    i, res = 0, ""

    while i < len(line):
        if line[i].isdigit():
            return line[i]

        substring, j = "", 0
        while i + j < len(line):
            substring += line[i + j]
            if substring in digits:
                return digits[substring]
            if not reduce(
                lambda x, y: x + 1 if y.startswith(substring) else x, digits.keys(), 0
            ):
                break
            j += 1
        i += 1
    return res


def answer_1() -> int:
    res = 0
    with open("data.txt") as data:
        for line in data:
            stripped_line = reduce(lambda x, y: x + y if y.isdigit() else x, line, "")
            res += int(stripped_line[0] + stripped_line[-1])
    return res


def answer_2() -> int:
    res = 0
    with open("data.txt") as data:
        for line in data:
            res += int(find_digit(line) + find_digit(line, reversed=True))
    return res


if __name__ == "__main__":
    print(f"Answer 1: {answer_1()}")
    print(f"Answer 2: {answer_2()}")
