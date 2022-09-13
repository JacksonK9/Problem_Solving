T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    q = list(map(int, input().split()))
    
    seq = 1
    
    while True:
        if q[0] >= max(q):
            if M == 0:
                print(seq)
                break
            else:
                seq += 1
                q.pop(0)
                M -= 1
                
        
        else:
            q.append(q.pop(0))
            if M == 0:
                M = len(q) - 1
            else:
                M -= 1