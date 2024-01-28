# 5 5 5 5 5
# 5 5 5 5
# 5 5 5
# 5 5
# 5
# for i in range(5,0, -1):
#         b = 5
#         for n in range(1, i + 1):
#             print(b, end=' ')
#         print(" ")

# 5 5 5 5 5
# 4 4 4 4
# 3 3 3
# 2 2
# 1
# for i in range(5,0,-1):
#     n= i
#     for o in range(0,i):
#         print(n, end=' ')
#     print(" ")

# 1
# 3 3
# 5 5 5
# 7 7 7 7
# 9 9 9 9 9
# for i in range(1, 5+1):
#     for o in range(i):
#         print((i * 2 - 1), end=" ")
#     print()

# 1
# 2 1
# 3 2 1
# 4 3 2 1
# 5 4 3 2 1
# for i in range(1,6):
#     for n in range(i, 0, -1):
#         print(n, end=' ')
#     print(" ")



# * * * * *
#  * * * *
#   * * *
#    * *
#     *
#    * *
#   * * *
#  * * * *
# * * * * *
# for i in range(5):
#     print(" " * i, end="")
#     print("* " * (5 - i))
# for i in range(5 - 2, -1, -1):
#     print(" " * i, end="")
#     print("* " * (5 - i))


# DRAFT BELOW
# num = 1
# for r in range(1, 5):
#     for c in range(r,):
#         print(num, end=' ')
#         num += 1
#     print()


# counter = 0
# for i in range(1,8,2):
#     counter = counter + 1
#     for j in range(0,counter):
#         print(i-j,end = " ")
#     print()


# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1
# rows = 5
# for i in range(1,rows+1):
#     for s in range(1, i+1):
#         print(s, end=" ")
#     print()
#
# for i in range(rows-1,0,-1):
#     for s in range(1,i+1):
#         print(s, end=" ")
#     print()


# * * * * * * * * *
#   * * * * * * *
#     * * * * *
#       * * *
#         *
#         *
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *
counter = 1
rows = 5
for row in range(rows,0,-1):
    for space in range(rows-row,0,-1):
        print(" ", end=" ")

    for star in range(1, row * 2):
        print("*", end=" ")
    print()

for row in range(1,rows+1):
    for space in range(rows-row,0,-1):
        print(" ", end=" ")

    for star in range(1,row*2):
        print("*", end=" ")
    print()
