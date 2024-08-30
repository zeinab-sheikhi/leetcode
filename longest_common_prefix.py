def longestCommonPrefix(strs):
    """
        :type strs: List[str]
        :rtype: str
    """
    # First Solution, Runtime: 8 ms
    # clp = ""
    # i = 0
    # print(sorted(strs))
    # first_item = strs[0]
    # while i < min(len(item) for item in strs):
    #     j = 1
    #     prefix = first_item[i]
    #     while j < len(strs):
    #         if prefix != strs[j][i]:
    #             return clp
    #         j += 1
    #     clp += prefix
    #     i += 1
    
    # return clp

    # Better Solution

    sorted_list = sorted(strs)
    clp = ""
    first = sorted_list[0]
    last = sorted_list[-1]
    for i in range(min(len(first), len(last))):
        if first[i] != last[i]:
            return clp 
        clp += first[i]
    return clp


if __name__ == '__main__':
    res = longestCommonPrefix(strs=["flower", "flow", "flight"])
    # res = longestCommonPrefix(strs=["dog", "racecar", "car"])
    print(res)
