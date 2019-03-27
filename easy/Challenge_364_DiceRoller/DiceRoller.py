import random

def getInput(fileName):
    with open(fileName) as f:
        content = f.readlines()

    content = [x.strip() for x in content]
    return parseInput(content)

def parseInput(content):
    toReturn = list()
    for die in content:
        toReturn.append(die.split('d'))
    return toReturn

def main():
    content = getInput("test.txt")
    rolls = list()
    for con in content:
        total = 0
        for x in range(int(con[0])):
            i = random.randint(1,int(con[1]))
            total += i
            rolls.append(i)

        print(str(total) + " | ", end = " ")
        for i in rolls:
            print(i, end = " ")
        print("")
        rolls = list()

if __name__ == "__main__":
    main()
