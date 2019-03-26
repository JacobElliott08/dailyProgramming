def main():
    print(balancedBonus(""))
    print(balancedBonus("abc"))
    print(balancedBonus("abcabcabcabcabcabcabc"))
    print(balancedBonus("onetwothreefourfivesix"))
    print(balancedBonus("watchmewalkaway"))


def balanced(string):
    return string.count("x") == string.count("y")

def  balancedBonus(string):
    strDict = dict()
    for c in string:
        if(c not in strDict):
            strDict[c] = 1
        else:
            strDict[c] += 1

    ourValues = list(strDict.values())
    if(len(ourValues) == 0):
        return True

    capVal = ourValues[0]
    for i in ourValues:
        if(i != capVal):
            return False
    return True




if __name__ == "__main__":
    main()
