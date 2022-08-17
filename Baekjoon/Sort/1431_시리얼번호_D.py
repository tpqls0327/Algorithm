arr = []
for _ in range(int(input())):
    word = input()
    s = sum(map(int, filter(lambda x: x in '123456789', word)))
    arr.append([word, s])

arr.sort(key=lambda x: [len(x[0]), x[1], x[0]])
for i, _ in arr:
    print(i)
