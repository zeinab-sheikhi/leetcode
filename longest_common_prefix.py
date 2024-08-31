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
    # while i < len(min(strs)):
    #     j = 1
    #     prefix = first_item[i]
    #     while j < len(strs):
    #         if prefix != strs[j][i]:
    #             return clp
    #         j += 1
    #     clp += prefix
    #     i += 1
    
    # return clp

    # Revised version

    clp = ""
    for i in range(len(min(strs))):
        prefix = strs[0][i]
        for j in range(len(strs)):
            if prefix != strs[j][i]:
                return clp
        clp += prefix
    return clp


    # Other Solutions
    
    # sorted_list = sorted(strs)
    # clp = ""
    # first = sorted_list[0]
    # last = sorted_list[-1]
    # for i in range(min(len(first), len(last))):
    #     if first[i] != last[i]:
    #         return clp 
    #     clp += first[i]
    # return clp

    # prefix = strs[0]
    # for string in strs[1:]:
    #     print(" the string is: ", string)
    #     while string.find(prefix) != 0:
    #         print(f"enter the while loop for this string and {string.find(prefix)}")
    #         prefix = prefix[:-1]
    #         print("The prefix is: ", prefix)
    #     if not prefix:
    #         return ""
    # return prefix


if __name__ == '__main__':
    res = longestCommonPrefix(strs=["flower", "flow", "flight"])
    # res = longestCommonPrefix(strs=["dog", "racecar", "car"])
    print(res)
