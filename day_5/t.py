data = [
    1044452533,
    40389941,
    3710737290,
    407166728,
    1552449232,
    639689359,
    3327654041,
    26912583,
    3440484265,
    219136668,
    1126550158,
    296212400,
    2332393052,
    229950158,
    200575068,
    532702401,
    4163696272,
    44707860,
    3067657312,
    45353528,
]

count = 0
for i, val in enumerate(data):
    if i % 2:
        continue
    count += val

for j in range(count):
    if not j % 100000:
        print(f"{j} / {count}")

print(count)
