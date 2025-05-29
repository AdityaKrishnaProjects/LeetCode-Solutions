def combine(n, k):
    """
    return number of k combinations of n
    """

    def factorial(n, i):
        factorial = 1

        for _ in range(i):
            factorial *= n
            n -= 1

        return factorial

    res = [[] for _ in (factorial(n, k)//factorial(k, k))]
    count = [[0] for _ in range(n)]
        
    


print(combine(4, 2))
print(combine(1, 1))
print(combine(5, 5))