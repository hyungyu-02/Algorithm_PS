#tree, recursion
import sys
input = sys.stdin.readline

N = int(input())
tree = {}
for i in range(N):
    root, l, r = map(str, input().split())
    tree[root] = [l, r]

def preorder(root):
    print(root, end='')
    if not tree[root][0] == '.':
        preorder(tree[root][0])
    if not tree[root][1] == '.':
        preorder(tree[root][1])
def inorder(root):
    if not tree[root][0] == '.':
        inorder(tree[root][0])
    print(root, end='')
    if not tree[root][1] == '.':
        inorder(tree[root][1])
def postorder(root):
    if not tree[root][0] == '.':
        postorder(tree[root][0])
    if not tree[root][1] == '.':
        postorder(tree[root][1])
    print(root, end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')
