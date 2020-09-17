#! python 3

# with open('src/cities.txt', 'a') as city_file:
#     for i in range(0, 12):
#         print("{:<2} times {:>2} is {:^80}".format(i + 1, 1000, (i + 1) * 1000),file=city_file)
#     print("_" * 40,file=city_file)

# message = "Hello, welcome!\nThis is some text that should be centered!"
# print('\n'.join('{:^80}'.format(s) for s in message.split('\n')))
# print('\n'.join(message))
# print(message.split('\n'))

print("Jan: {2}, Feb: {0}, Mar: {2}, Apr: {1}, May: {2}, Jun: {1}, Jul: {2}, Aug: {2}, Sep: {30}, Oct: {2}, Nov: {1}, Dec: {2}"
    .format(28, 30, 31))