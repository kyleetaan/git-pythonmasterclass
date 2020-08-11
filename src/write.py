#! python 3

with open('src/cities.txt', 'a') as city_file:
    for i in range(0, 12):
        print("{:<2} times {:>2} is {:<2}".format(i + 1, 2, (i + 1) * 2),file=city_file)
    print("_" * 40,file=city_file)