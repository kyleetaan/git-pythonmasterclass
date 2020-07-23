data = [104, 101, 4, 110, 308, 103, 7, 108,
        5, 105, 100, 309, 107, 106, 102, 109]
min_valid = 100
max_valid = 200

# for index in range(len(data) - 1, -1 , -1):
#     if data[index] < min_valid or data[index] > max_valid:
#         print(index, data)
#         del data[index]
top_index = len(data) - 1
for index, value in enumerate(reversed(data)):
    if value < min_valid or value > max_valid:
        print(top_index - index, value)
        del data[top_index - index]

print(data)