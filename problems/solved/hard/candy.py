# Requirements are not restrictive, indices must only have more candy than 
# neighbors with lower rating. Candies given only grows as a result of runs of 
# strictly increasing numbers. When the sequence decreases or is equal to the 
# previous value, candy given can be reset to 1. When two increasing runs meet, 
# use the max value to ensure that both neighbor conditions are satisfied.
def candy(ratings):

    N = len(ratings)
    candies = [float("-inf")] * N

    if N == 1:
        return 1

    def identifyLocalMinima(nums):
        res = []
        
        for i in range(N):
            if i == 0:
                if nums[i] < nums[i+1]:
                    res.append(i)
                continue

            if i == N-1:
                if nums[N-1] < nums[N-2]:
                    res.append(i)
                continue
            
            if (nums[i] < nums[i - 1] and nums[i] < nums[i + 1]) or (nums[i] < nums[i - 1] and nums[i] == nums[i + 1]) or (nums[i] == nums[i - 1] and nums[i] < nums[i + 1]):
                res.append(i)
                
        return res

    minima = identifyLocalMinima(ratings)

    def expansion(i):
        curr = 1
        candies[i] = 1
        initial_i = i

        while i < N:
            if i+1 < N:
                if ratings[i+1] <= ratings[i]:
                    break
                if ratings[i+1] > ratings[i]:
                    curr += 1
                candies[i+1] = max(curr, candies[i+1])
            i = i+1

        i = initial_i
        curr = 1

        while i > 0:
            if i-1 >= 0:
                if ratings[i-1] <= ratings[i]:
                    break
                if ratings[i-1] > ratings[i]:
                    curr += 1
                candies[i-1] = max(curr, candies[i-1])
            i = i-1

    for i in minima:
        expansion(i)

    for i, n in enumerate(candies):
        if n == float("-inf"):
            candies[i] = 1

    return sum(candies)

print(candy([1,0,2]))
print(candy([1,2,2]))
print(candy([0,1,0,2,1,0]))
print(candy([0,2,4,6,4,6,6,0]))
print(candy([0,2,4,6,3,2,1,0]))
print(candy([1,2,3,5,4,3,2,1,4,3,2,1,3,2,1,1,2,3,4]))
print(candy([1,6,6,6,3,2,1]))