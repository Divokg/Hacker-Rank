"""arr = [1,2,3,4,5]

def miniMaxSum(arr):
    arrf = arr
    arrf.sort()
    min_sum = (sum(arrf) - arrf[-1])
    max_sum = (sum(arrf) - arrf[0])
    
    print(min_sum,max_sum)    

miniMaxSum(arr)
    
"""

"""
def timeConversion(s):
    if s[-2:] == "PM" and s[:2] == "12":
        print (s[:8])
        return (s[:8])
    elif s[-2:] == "PM":
        hr_pm = int(s[:2]) + 12
        str_hr_pm = str(hr_pm)
        print (str_hr_pm + s[2:8])
        return (str_hr_pm + s[2:8])
    elif s[-2:] == "AM" and s[:2] == "12":
        hr_am = int(s[:2]) - 12
        str_hr_am = str(hr_am).zfill(2)
        print (str_hr_am + s[2:8])
        return (str_hr_am + s[2:8])
    else:
        print (s[:8])
        return (s[:8])




string = "01100110 01101001 01101110 01100100 00101110 01100110 01101111 01101111 00101111 01101110 01100001 01101001 01110010 01101111 01100010 01101001 00110010 00110010"

b'string'.decode('ascii')


timeConversion("12:05:45AM")

"""
"""import math
import os
import random
import re
import sys

#
# Complete the 'matchingStrings' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY strings
#  2. STRING_ARRAY queries
#

def matchingStrings(strings, queries):
    results = []
    
    for query in range(len(queries)):
        print(queries[query])
        for string in range(len(strings)):
            count = 0
            if queries[query] == strings[string]:
                count += 1
        results.append(count)
        


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    strings_count = int(input().strip())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
    """
"""
def flippingBits(n):
    bin_n = list(bin(n))
    print( "bin_n =" + bin_n)
    bin_new = bin_n.remove(0)
    print(bin_new)
    new_b = bin_new.remove("b")
    print(new_b)
    bin_str_32 = str(bin_n).zfill(32)
    bin_int_32 = int(bin_str_32)
    
    
    for i in range(len(bin_int_32)):
        if i == 0:
            bin_int_32[i] = bin_int_32[i] + 1
        else:
            bin_int_32[i] = bin_int_32[i] - 1
        
    integer = int(bin_int_32)
    return integer


flippingBits(12)
"""

def calPoints(ops) -> int:
    num = int
    cancel = "C"
    double = "D"
    plus = "+"
    result = None
    score = []
    
    for i in range(len(ops)):
        
        if ops[i] == double:
            dabo = score[-1]*2
            score.append(dabo)
        elif ops[i] == cancel:
            score = score[:-1]
        elif ops[i] == plus:
            add = score[-1] + score[-2]
            score.append(add)
        else:
            score.append(int(ops[i]))
    
    print ("score is",score)
    print (sum(score))
calPoints(["5","2","C","D","+"])