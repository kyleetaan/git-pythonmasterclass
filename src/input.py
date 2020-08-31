# romeo_juliet = open("../../../Python/qractice/romeoandjuliet.txt", "r")

# for line in romeo_juliet:
#     print(line)
# romeo_juliet.close()

# with open("../../../Python/qractice/romeoandjuliet.txt", "r") as rj:
#     line = rj.readline()
#     while line:
#         print(line, end = '')
#         line = rj.readline()

# with open("../../../Python/qractice/romeoandjuliet.txt", "r") as rj:
#     lines = rj.readlines()

# for line in lines[::-1]:
#     print(line, end = "")

with open(r"C:\Users\PC\Documents\Python\qractice\romeoandjuliet.txt", "r") as rj:
    lines = rj.read()

for line in lines[::-1]:
    print(line, end = "") 