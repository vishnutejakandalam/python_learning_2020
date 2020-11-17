str = "ma/he/sh"
sep = "/"
def split(str,sep):
    result = []
    temp = ""
    for x in str:
        if x!= sep:
            temp+=x
        else:
            result.append(temp)
            temp = ""
    result.append(temp)
    return result

