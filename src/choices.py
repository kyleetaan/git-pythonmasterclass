list = ['Learn Python', 'Learn Java', 'Go swimming', 'Have dinner', 'Go to bed', 'Do a handstand', 'Jump', 'Run', 'Breath']

answer = None
while True:
    if answer == '0':
        break

    print('Please choose your option from the list below:\n')
    for i in range(len(list)): 
        print('{}. {}'.format(i + 1, list[i]))
    answer = int(input('0. Exit\n'))

    print()
    print('Your input is {}'.format(answer))

    if answer in range(len(list) + 1):
        print('{}'.format(list[answer-1]))
else:
    print('Thanks for taking part in this.')