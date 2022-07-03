n = int(input())
for _ in range(n):
    b_arr = [0 for _ in range(26)]
    a_arr = [0 for _ in range(26)]

    b, a = input().split()
    for i in a:
        b_arr[97 - ord(i)] += 1
    for j in b:
        a_arr[97 - ord(j)] += 1

    print("Possible" if b_arr == a_arr else "Impossible")
