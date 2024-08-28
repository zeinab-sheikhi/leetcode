def is_palindrome(x):
    """
        :type x: int
        :rtype: bool
    """
    
    ###### My Solutions #######

    # First Solution, Runtime: 66 ms
    # if x < 0:
    #     return False

    # x_list = []
    # tmp = x
    # while tmp != 0:
    #     res = tmp % 10
    #     tmp = tmp // 10
    #     x_list.append(res)

    # size = len(x_list) - 1
    # new_x = 0

    # for d in x_list:
    #     if size >= 0:
    #         new_x = d * (10 ** size) + new_x
    #     size = size - 1

    # return new_x == x
    
    # Second Solution, Runtime: 42 ms
    # tmp = [digit for digit in str(x)]
    # original_list = tmp[:]
    # tmp.reverse()
    # if original_list == tmp:
    #     return True
    # return False

    # Second Solution, cleaner version, Runtime: 32 ms
    # return str(x) == str(x)[::-1]

    # Third Solution, Runtime: 52 ms
    # tmp = [digit for digit in str(x)]
    # i = 0
    # j = len(tmp) - 1

    # while i < len(tmp) and j > 0:
    #     if tmp[i] != tmp[j]:
    #         return False
            
    #     i = i + 1
    #     j = j - 1

    # return True

    # Fourth Solution: Runtime: 63 ms
    # tmp = [digit for digit in str(x)]
    
    # while tmp != []:
    #     if tmp[0] != tmp[-1]:
    #         return False
    #     else:
    #         try:
    #             tmp.pop()
    #             tmp.pop(0)
    #         except IndexError:
    #             print()
    # return True

    ##### Other Solutions ######
    if x % 10 == 0 or x < 0:
        return False
    rev = 0
    tmp = x
    
    while tmp != 0:
        rev = rev * 10 + tmp % 10
        tmp //= 10
    
    return x == rev

if __name__ == '__main__':
    res = is_palindrome(x=-123210)
    print(res)
