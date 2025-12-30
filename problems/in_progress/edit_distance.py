def minDistance(word1, word2):
    pass

"""
we have three operations, insert delete and replace. We prefer to replace rather 
than inserting or deleting, as the cost of inserting and deleting is two 
operations, whereas replacement only costs one. We must end with the final 
string, so preserving as many characters as we can in their original position 
is the cheapest option, costing 0 operations. 

Given that this is the case the first thing we must do is iterate through word1 
and find the longest substring that contains the maximum number of chars in the correct 
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
word1: "mosrllrs"

Insertion has an effective cost of +1. Replacement does not (when we insert to 
the end or middle, that means there is an extra char that will have to be 
deleted eventually, replacing means that that char does not need to be deleted).




"""