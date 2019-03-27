import random

def getWords(length):
    with open("./../../resource/words.txt") as file:
        words = [x for x in map(str.strip, file.readlines()) if len(x) == length]
    return words

def pickWords(difficulty):
    difficulties = {1 : [5,6], 2 : [7,8], 3 : [9,10], 4 : [11,12], 5 : [13,14,15]}
    words = (getWords((difficulties[difficulty])[random.randint(0,len(difficulties[difficulty])-1)]))
    random.shuffle(words)
    words = words[:(difficulties[difficulty])[random.randint(0,len(difficulties[difficulty])-1)]]
    return words

def countGuess(wordOne, wordTwo):
    return len([x for x in range(0,len(wordOne)) if wordOne[x] == wordTwo[x]])


def main():
    #ask for difficulty
    attemps = 0
    difficulty = int(input("Difficulty (1-5) ? "))
    potentialWords = pickWords((difficulty))
    actualWord = potentialWords[random.randint(0,len(potentialWords) - 1)]

    while(attemps < 3):
        print("Potential Words : ")
        for x in potentialWords:
            print(x)
        print(" ")

        #print("Acutal Word : ")
        #print(actualWord)

        guess = input("Guess Words: ").strip()
        correctAmount = countGuess(guess,actualWord)
        if(correctAmount == len(actualWord)):
            print("Word Found")
            break
        else:
            print("Inccorect : "+str(correctAmount)+"/"+ str(len(actualWord)))
            print(" ")
        attemps += 1



if __name__ == '__main__':
    main()
