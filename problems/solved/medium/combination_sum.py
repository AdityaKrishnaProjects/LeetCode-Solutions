# backtracking so worst case is all possible candidate solutions are entertained.
def combinationSum(candidates, target):
    
    candidates.sort(reverse=True)
    N = len(candidates)
    res = []

    def pathTakeIndexAndAmount(path, index, amount):
        if amount == 0:
            res.append(path[:])
            return
        
        if index == N:
            return
        
        # take
        if amount - candidates[index] >= 0:
            path.append(candidates[index])
            pathTakeIndexAndAmount(path, index, amount - candidates[index])
            path.pop()
        
        # skip
        pathTakeIndexAndAmount(path, index+1, amount)

    pathTakeIndexAndAmount([], 0, target)

    return res

print(combinationSum([2,3,6,7], 7))
print(combinationSum([2,3,5], 8))
print(combinationSum([2], 1))