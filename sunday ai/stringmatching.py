from fuzzywuzzy import fuzz
import Levenshtein as lev
import numpy as np
from fuzzywuzzy import process

str2Match = "apple inc.."
strOptions = ["Apple In","apple park","apple incorporated","iphone" , "applle" , "appal"]
Ratios = process.extract(str2Match,strOptions)
print(Ratios)
# You can also select the string with the highest matching percentage
highest = process.extractOne(str2Match,strOptions)
print(highest)

Str1 = "apple inc.."
Str2 = "applle"
Ratio = fuzz.ratio(Str1.lower(),Str2.lower())
Partial_Ratio = fuzz.partial_ratio(Str1.lower(),Str2.lower())
Token_Sort_Ratio = fuzz.token_sort_ratio(Str1,Str2)
Token_Set_Ratio = fuzz.token_set_ratio(Str1,Str2)
print(Ratio)
print(Partial_Ratio)
print(Token_Sort_Ratio)
print(Token_Set_Ratio)