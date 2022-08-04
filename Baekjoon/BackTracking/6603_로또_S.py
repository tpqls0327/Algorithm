# 6603 로또 

def back(start, idx):
    if idx == 6:
        for i in range(6):
            print(arr[i], end=' ')
        print()
        return
    for i in range(start, len(data)):
        arr[idx] = data[i]
        back(i + 1, idx + 1)

arr = [0 for i in range(13)]
while True:
    data = list(map(int, input().split()))
    if data[0] == 0:
        break
    del data[0]
    back(0, 0)
    print()
