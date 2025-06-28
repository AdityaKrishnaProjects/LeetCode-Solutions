# uses backtracking to implement permutations
def permute(nums):

    N = len(nums)
    res = []

    def path_gen(path, seen):
        if len(path) == N:
            res.append(path[:])
        
        for i in range(N):
            if i not in seen:
                seen.add(i)
                path.append(nums[i])
                path_gen(path, seen)
                path.pop()
                seen.remove(i)

    path_gen([], set())

    return res