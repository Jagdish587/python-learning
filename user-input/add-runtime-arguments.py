from sys import argv

add = 0

n = len(argv) 

print(f"len val = {n}")

for i in range(1, n):
    add = add + int(argv[i])

print(f" addition value = {add}")