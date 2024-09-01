def isValid(s):
    """
        :type s: str
        :rtype: bool
    """

    stack = []

    matching_paranthesis = {")": "(", "]": "[", "}": "{"}

    for char in s:
        if char in matching_paranthesis.values():
            stack.append(char)
        elif char in matching_paranthesis:
            if not stack or stack[-1] == matching_paranthesis[char]:
                return False
            stack.pop()
    return not stack



    # chars_mapping = {
    #     "(": ")", 
    #     "[": "]", 
    #     "{": "}", 
    # }


    # else:
    #     first_list = s[:middle_index]
    #     second_list = s[middle_index:]

    #     print("*******")
    #     print(first_list)
    #     print(second_list)

    
    # index = 0
    # while len(s) != 0:
    #     char = s[index]
    #     if char in chars_mapping.keys():
    #         close = chars_mapping[char]
    #         if close in s[::-1]:
    #             close_index = len(s) - s[::-1].index(close) - 1
                
    #             print("rest is: ", s[index + 1: close_index])

    #             if len(s[index + 1: close_index]) % 2 == 0:
    #                 char_list = list(s)
    #                 char_list.pop(close_index)
    #                 char_list.pop(index)
    #                 s = ''.join(char_list)
    #                 print(s)
    #                 print("\n")
                
    #             else:
    #                 return False
                
                # if len(s) % 2 != 0:
                #     return False
        # else:
        #     return False    
    # for index, char in enumerate(s):
    #     if char in chars_mapping.keys():
    #         close = chars_mapping[char]
    #         if close in s[::-1]:
    #             close_index = len(s) - s[::-1].index(close)

    #             print(char)
    #             print(close)
    #             s = s[index + 1:close_index - 1]
    #             if len(s) % 2 != 0:
    #                 return False
    #             # print(s[index + 1:close_index - 1])
    #             # print(len(s[index + 1:close_index]))
    #             # print(index)
    #             # print(s.index(close))
    #             print('\n')
    #         # print(char)
            # print(s.find(chars_mapping[char]))



    # positions = []
    # occurrences = {}
    
    # for index, char in enumerate(s):
    #     rest = s[index + 1:]
    #     if char in chars_mapping.keys():
    #         close = chars_mapping[char]
    #         if rest is None or close not in rest:
    #             return False
    #         else:
    #             close_index = rest.index(close) + index + 1 
    #             if close_index - index > 1:
    #                 positions.append((index, close_index))

    #     if char in occurrences:
    #         occurrences[char] += 1
    #     else:
    #         occurrences[char] = 1
    
    # print(positions)
    # print(occurrences)

    # if len(occurrences.keys()) % 2 != 0:
    #     return False
    
    # for k, v in occurrences.items():
    #     if k in chars_mapping.keys():
    #         close = chars_mapping[k]
    #         if close not in occurrences.keys() or occurrences[close] != v:
    #             return False
    #         else: 
    #             return True

    # for idx, item in enumerate(positions):
    #     for next_item in positions[idx + 1:]:
    #         print(item)
    #         print(next_item)
    #         if item[0] < next_item[0] and item[1] < next_item[1]:
    #             print("this must run")
    #             return False

    # return True


if __name__ == '__main__':
    # s = ")"
    # s = "()"
    # s = "(]"
    # s = "()[]{}"
    # s = "([])"
    # s = ")[(]"
    # s = "(){}}{"
    # s = "(){}{}"
    # s = "({{{{}}}))"
    # s = "]()"
    # s = "([)]"
    s = "[({(())}[()])]"
    # s = "(("
    s = "({[})]"
    res = isValid(s)
    print(res)
