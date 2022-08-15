from fuzzywuzzy import fuzz
import Levenshtein as lev
import numpy as np
from fuzzywuzzy import process

f = open("sunday.txt","r")


#r = f.readline()
Command = ""

s = f.readlines()
print(s[0])
i=0
ratioss = [None] * len(s)
while(i<len(s)):
    y = s[i].split(" ans")
    Token_Set_Ratio = fuzz.token_set_ratio(Command,y[0])
    ratioss[i] = Token_Set_Ratio 
    
    i = i + 1 
j = max(ratioss)
'''
x = s[j].split("ans ")
print(x[j] , end="")
'''
print(j)
print(ratioss)

max_item = max(ratioss)
k = [index for index, item in enumerate(ratioss) if item == max_item]
print(k[0])
x = s[k[0]].split("ans ")
print(x[1] , end="")
f.close()

'''s = f.readlines()
print(s[0])
i=0
while(i<len(s)):
    y = s[i].split(" ans")
    if(Command in y[0]):
        x = s[i].split("ans ")

        print(x[1] , end="")
    
    i = i + 1 

f.close()
'''
'''
with open('sunday.txt' , 'r') as f:

    for line in f:
        print(line)
        print(line)'''