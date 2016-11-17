class Common:
    def __init__(self):
        pass

    # str 대상문자열
    # quarterIdx 자르기 기준
    def seperate(self, str, quarterIdx):
        tmp = str.split(",")
        result = tmp[0:quarterIdx - 1]
        result.append(str.replace(",".join(tmp[0:quarterIdx - 1]), ""))
        return result

