import os

with open('sample.txt', 'r') as f:
    for row in f:
        print(row.strip())
        if os.path.exists(row.strip()):
            continue
        else:
            os.mkdir(row.strip())
