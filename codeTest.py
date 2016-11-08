def seperate3quarter(str):
    result =  str.split(",")
    result = result[0:2].append(str.replace((result[0] + "," + result[1] + "," ),""))
    return result
