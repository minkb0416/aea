sample = [1, 11, 22, -20, 55, -33, 0, -5, 12, 35, 19, -19, -9, -1, -100, 90]
negative_val = []

for num in sample:
    if 10< num < 50:
        negative_val.append(num)

print(negative_val)