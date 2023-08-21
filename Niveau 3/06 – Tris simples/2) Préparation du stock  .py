n, m = map(int, input().split())
stock = list(map(int, input().split()))
new_liste= list(map(int, input().split()))
indices = []
for i in new_liste:
    index = 0
    while index < n and stock[index] < i:
        index += 1
    indices.append(index)
    stock.insert(index, i)
    n += 1
print(" ".join(str(i) for i in indices))
print(" ".join(str(i) for i in stock))