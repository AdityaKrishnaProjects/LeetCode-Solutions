### Preface

This note will include general notes on algorithms learned from doing LeetCode problems. 

### Notes on Recursion

Any program using iteration can instead use recursion. When using recursion to solve a problem we must pay attention to ensuring that we pass the values that we will be using in our algorithm, and that at each function call the algorithm makes the subproblems smaller. This is how we ensure that our algorithms will terminate at our base case. 

We can have recursive algorithms perform operations in the same order as iterative algorithms by implementing a helper function. This helper function in effect plays the rool of the iterative loop. 