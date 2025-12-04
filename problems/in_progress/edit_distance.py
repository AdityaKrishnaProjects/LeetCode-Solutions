def minDistance(word1, word2):
    pass

"""
we have three operations, insert delete and replace. We prefer to replace rather 
than inserting or deleting, as the cost of inserting and deleting is two 
operations, whereas replacement only costs one. We must end with the final 
string, so preserving as many characters as we can in their original position 
is the cheapest option, costing 0 operations. 

Given that this is the case the first thing we must do is iterate through word1 
and find the substring that contains the maximum number of chars in the correct 
order. In essence, we'd like to find the substring with the lowest cost of 
completion in terms of replacement and insertion. Consider the following example:

word2: "rost"

word1:"rosmanrosburrost"
word1:"roelwaystbarosn"
word1:"rominstburos"
word1:"minburo" replace: cost 7, insert: cost 7

word2: "rosti"
word1:"romtilroslltl"

word2: "rosti"
word1:"omroptilrost" 8 middle, 9 end

word2: "ros"
word1: "mosrllrons"






"""