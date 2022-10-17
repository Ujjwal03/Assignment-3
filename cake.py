

import math
import os
import random
import re
import sys



def birthdayCakeCandles(candles):
    n=max(candles)
    count=0
    for i in range(0,len(candles)):
        if (candles[i]==n): 
            count+=1
    return count       
    
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()
