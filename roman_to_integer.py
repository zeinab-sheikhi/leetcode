def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    res = 0
    
    # i = 0
    # roman_to_value = {
    #     "I": 1, "IV": 4, "IX": 9, "V": 5, "X": 10, "XL": 40, "XC": 90, "L": 50, "C": 100, "CD": 400, "CM": 900, "D": 500, "M": 1000
    # }   

    # while i < len(s):
    #     if i + 1 < len(s) and s[i:i + 2] in roman_to_value:
    #         res += roman_to_value[s[i:i + 2]]
    #         i += 2
    #     else:
    #         res += roman_to_value[s[i]]
    #         i += 1
    
    # return res

    # Clean version

    roman = {
        'I': 1, 
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }

    for i in range(len(s)):
        if i < len(s) - 1 and roman[s[i]] < roman[s[i + 1]]:
            res -= roman[s[i]]
        else:
            res += roman[s[i]]
    
    return res
    

if __name__ == '__main__':
    res = romanToInt(s="III")
    # res = romanToInt(s="LVIII")
    # res = romanToInt(s="MCMXCIV")
    print(res)
