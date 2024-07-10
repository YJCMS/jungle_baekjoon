# n을 두 소수의 합으로 표현
# 두 소수의 차이가 가장 작아야함
# n//2값으로 두개의 변수를 생성하고 각 플러스마이너스해서 소수인지 판별 후 합
def isPrime(n):
    if n == 1: return False
    if n == 2: return True
    for i in range(2, int(n**1/2)+1):
        if n%i == 0 : return False
    return True

round = int(input())
for i in range(round):
    n = int(input())
    a = n//2
    b = n//2

    while True:
        if isPrime(a) and isPrime(b):
            break
        a -= 1
        b += 1
        
    print(a, b)