#Sorting, set
import sys
#sys.stdin.readline()

n = int(sys.stdin.readline())

lst = []

for i in range(n):
    lst.append(sys.stdin.readline().strip())
set_lst = set(lst)
lst = list(set_lst)

lst.sort()
lst.sort(key = len)

for i in range(len(lst)):
    print(lst[i])
