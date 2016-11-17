#use jpype
str = "1,2,3,456,789,0"

import os

os.system("set")



# 자르기 기준
division_idx = 3

tmp = str.split(",")
result = tmp[0:division_idx-1]
result.append(str.replace( ",".join(tmp[0:division_idx-1]) , ""))
print(result)


