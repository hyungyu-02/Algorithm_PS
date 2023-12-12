#Binary Search, 재귀
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

#재귀를 이용해 왼쪽, 오른쪽 서브트리는 재귀함수에 다시 호출하고 루트는 그대로 출력
def printRoot(start,end):
    if start > end:
        return
    root = arr[start]
    pin = end + 1
    for i in range(start+1, end+1):
        if root < arr[i]:
            pin = i
            break
    printRoot(start+1,pin-1)
    printRoot(pin,end)
    print(root)

arr =[]

while True:
    try:
        arr.append(int(input()))
    except:
        break

printRoot(0,len(arr)-1)
