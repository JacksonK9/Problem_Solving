N, K = map(int, input().split())

def factorial(_n):
    if _n <= 1:
        return 1
    else:
        return _n * factorial(_n - 1)
        
print(int(factorial(N) / factorial(K) / factorial(N - K)))