def iso (uno, dos):
    if len(uno) != len(dos):
        return False
    hash = {}
    rec = set()
    x = len(uno)
    y= range(len(uno))
    for i in range(len(uno)):
        if uno[i] in hash:
            if hash[uno[i]] != dos[i]:
                return False
        else:
            if dos[i] in rec:
                return False
            hash[uno[i]] = dos[i]
            rec.add(dos[i])
    return True

str_1 = "Mysdd"
str_2 = "sdfll"
iso(str_1, str_2)