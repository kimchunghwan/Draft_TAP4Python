class Common:
    def __init__(self):
        pass

    def seperate_bisect(self,str):
        tmp = str.split(",")
        result = tmp[0:1]
        result.append(str.replace((tmp[0] + ","), ""))
        return result

    def seperate_3quarter(self,str):
        tmp = str.split(",")
        result = tmp[0:2]
        result.append(str.replace((tmp[0] + "," + tmp[1] + ","), ""))
        return result

    def seperate_quarter(self,str):
        tmp = str.split(",")
        result = tmp[0:3]
        result.append(str.replace((tmp[0] + "," + tmp[1] + "," + tmp[2] + ","), ""))
        return result
