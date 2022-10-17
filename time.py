import math
import os
import random
import re
import sys

def timeConversion(s):
    n=len(s)
    
    std=s.split(":")
    hour=std[0]
    mi=std[1]
    sec=s[(n-4):(n-2)]
    out=""
    if(s[(n-2):n]=="PM" and hour!="12"):
        temp=int(hour)
        temp+=12
        print(temp,mi,sec,sep=":",end="")
    elif(s[(n-2):n]=="AM" and hour=="12"):
        hour="00"
        print(hour,mi,sec,sep=":",end="")
    elif(s[(n-2):n]=="PM" and hour=="12"):
        print(hour,mi,sec,sep=":",end="")
    else:
        print(hour,mi,sec,sep=":",end="")
