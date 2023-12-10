from functools import reduce


def answer_1() -> int:
    res = 0

    with open("data.txt") as data:
        for line in data:
            matrix = [[int(c) for c in line.strip().split(" ")]]
            while any(m != 0 for m in matrix[-1]):
                old_row = matrix[-1]
                new_row = []
                i = 0
                while i < len(old_row) - 1:
                    new_row.append(old_row[i + 1] - old_row[i])
                    i += 1
                matrix.append(new_row)

            matrix[-1].append(0)
            j = len(matrix) - 2
            while j >= 0:
                matrix[j].append(matrix[j][-1] + matrix[j + 1][-1])
                j -= 1
            res += matrix[0][-1]
    return res


def answer_2() -> int:
    res = 0

    with open("data.txt") as data:
        for line in data:
            matrix = [[int(c) for c in line.strip().split(" ")]]
            while any(m != 0 for m in matrix[-1]):
                old_row = matrix[-1]
                new_row = []
                i = 0
                while i < len(old_row) - 1:
                    new_row.append(old_row[i + 1] - old_row[i])
                    i += 1
                matrix.append(new_row)

            matrix[-1] = [0, *matrix[-1]]
            j = len(matrix) - 2
            while j >= 0:
                matrix[j] = [matrix[j][0] - matrix[j + 1][0], *matrix[j]]
                j -= 1
            res += matrix[0][0]

    return res


if __name__ == "__main__":
    print("===================\n")
    print(f"Answer 1: {answer_1()}")
    print(f"Answer 2: {answer_2()}")
