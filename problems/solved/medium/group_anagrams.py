import collections

def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """

    c = collections.defaultdict(list)
    for s in strs:
        c["".join(sorted(s))].append(s)
    return c.values()

    ## Code below doesn't work because it doesn't account for duplicates. 
    ## Should use a counter like solution
    # anagram_dict = {}
    # N = len(strs)

    # for i in range(N):
    #     froz = frozenset(strs[i])
    #     if froz not in anagram_dict:
    #         anagram_dict[froz] = [i]
    #     else:
    #         anagram_dict[froz].append(i)

    # print(anagram_dict)

    # r_list = []
    # for ranges in anagram_dict.values():
    #     temp_list = []
    #     for i in ranges:
    #         temp_list.append(strs[i])
    #     r_list.append(temp_list)

    # return r_list

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(groupAnagrams([""]))
print(groupAnagrams(["a"]))
print(groupAnagrams(["ddddddddddg","dgggggggggg"]))