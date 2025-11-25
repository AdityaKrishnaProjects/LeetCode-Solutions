# need to figure out if starting at each possible start considering length of 
# word is less efficient than actually sliding the window char by char
def findSubstring(s, words):
    
    res = []
    i, j = 0, 0
    N = len(s)
    K = len(words)
    step = len(words[0])


"""
possible cases for pointers:

(con 1: no current candidate words inside interval)
    i and j should be equal

(valid in con 1, con 2: when j is on border of candidate word)
    j += step
        if s[j-step:j] is in dict:
            if val > 0
                dict[j-step:j] -= 1
                sat_count += 1 (con 2)
                if sat_count == K
                    res.append(i)
                    dict[s[i:i+step]] += 1
                    i += step
                    sat_count -= 1
            else:
                while s[i:i+step] != s[j-step:j]:
                    dict[s[i:i+step]] += 1
                    i += step
                    sat_count -= 1
                else:
                    i += step
                    sat_count -= 1
                
        else
            while sat_count > 0:
                dict[s[i:i+step]] += 1
                i += step
                sat_count -= 1
            i = j


foo | bar | the | bar | foo |thebarthefoobar

foo bar the the bar bar

foo tan men jin foo bar tan foo foo bar

aba bab aba bab aaa
"""

