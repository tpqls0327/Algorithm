# 13335 트럭

n,w,l = map(int,input().split())
truck = list(map(int, input().split()))
ans = 0  # 최단시간
bridge = []  # 다리위의 트럭
weight = 0   # 다리위 트럭 무게
idx = 0      # 트럭 인덱스 번호

while True:
    if idx == n:
        print(ans+w)
        break   
    if weight + truck[idx] <= l:
        if len(bridge) <= w:
            bridge.append(truck[idx])
            weight += truck[idx]
            idx += 1
            ans += 1             
        else:
            bridge.append(0)
            weight -= bridge[0]
            del bridge[0]    
    else:
        bridge.append(0)     
        ans += 1
        
    if len(bridge) >= w:
        weight -= bridge[0]
        del bridge[0]
