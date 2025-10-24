def PrimeList(N):
    if N <= 2:
        return ""
    # 初始化一个布尔列表，标记每个数是否为质数
    is_prime = [True] * N
    is_prime[0], is_prime[1] = False, False  # 0和1不是质数
    for i in range(2, int(N ** 0.5) + 1):
        if is_prime[i]:
            # 将i的所有倍数标记为非质数
            for j in range(i * i, N, i):
                is_prime[j] = False
    # 收集所有质数
    primes = [str(i) for i, prime in enumerate(is_prime) if prime]
    # 以空格分隔并返回
    return ' '.join(primes)
    
