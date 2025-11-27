from copy import deepcopy

# Sliding window tilted across all chars of starting word. 
def findSubstring(s, words):
    
    res = []
    i, j = 0, 0
    N = len(s)
    K = len(words)
    step = len(words[0])
    sat_count = 0
    sat = {}

    for word in words:
        if word in sat:
            sat[word] += 1
        else:
            sat[word] = 1

    for n in range(step):
        i += n
        j += n + step

        n_sat = deepcopy(sat)

        while j <= N:
            if s[j-step:j] in n_sat:
                if n_sat[s[j-step:j]] > 0:
                    n_sat[s[j-step:j]] -= 1
                    sat_count += 1
                    if sat_count == K:
                        res.append(i)
                        n_sat[s[i:i+step]] += 1
                        i += step
                        sat_count -= 1
                else:
                    while s[i:i+step] != s[j-step:j]:
                        n_sat[s[i:i+step]] += 1
                        i += step
                        sat_count -= 1
                    else:
                        i += step
            else:
                while sat_count > 0:
                    n_sat[s[i:i+step]] += 1
                    i += step
                    sat_count -= 1
                i = j

            j += step

        i, j = 0, 0
        sat_count = 0

    return res

# print(findSubstring("barfoothefoobarman", ["foo","bar"]))
# print(findSubstring("wordgoodgoodgoodbestword", ["word","good","best","word"]))
# print(findSubstring("barfoofoobarthefoobarman", ["bar","foo","the"]))
print(findSubstring("foobarthebarfoothebarthefoobar", ["bar","foo","the"]))
print(findSubstring("footanmenjinfoobartanfoofoobar", ["foo","foo","bar"]))
print(findSubstring("ababababababaaa", ["aba","bab","aba","bab"]))