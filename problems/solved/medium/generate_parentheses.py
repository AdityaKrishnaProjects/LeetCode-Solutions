# backtracking
def generateParenthesis(n):
    res = []

    def parenthesisAdder(string, left, right):
        if right == 0:
            res.append(string[:])
            return
        
        if left > 0:
            string += "("
            parenthesisAdder(string, left-1, right)
            string = string[:-1]
        
        if right > 0 and right > left:
            string += ")"
            parenthesisAdder(string, left, right-1)
            string = string[:-1]

    parenthesisAdder("", n, n)

    return res

print(generateParenthesis(3))
print(generateParenthesis(2))
print(generateParenthesis(1))
print(generateParenthesis(4))