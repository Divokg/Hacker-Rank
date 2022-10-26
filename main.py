arr = [1,2,3,4,5]

def miniMaxSum(arr):
    arrf = arr
    arrf.sort()
    min_sum = (sum(arrf) - arrf[-1])
    max_sum = (sum(arrf) - arrf[0])
    
    print(min_sum,max_sum)    

miniMaxSum(arr)
