list = input("Enter any number 100-999: ")
n1 =list[0:1]
n2 =list[1:2]
n3 = list[2:3]
n1 = int(n1)
n2 = int(n2)
n3 = int(n3)
list = int(list)
if n1 != 0:
    x = list % n1
else:
    x=1
if n2 != 0:
    y = list % n2
else:
    y=1
if n3 != 0:
    z = list % n3
else:
    z=1
if x == 0:
    print(list,"is divisible by ", n1)
if y == 0:
    print(list,"is divisible by ", n2)
if z == 0:
    print(list, "is divisible by ", n3)

