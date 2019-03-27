
def main():
    number = int(input("enter a number : "))

    print(gameOfThree(number))

def gameOfThree(number):
    if(number == 1):
        return 1

    if(int(number % 3) == 0):
        print(int(number))
        return gameOfThree(number/3)
    elif(int(number % 3) == 1):
        print(str(int(number)) + " - 1")
        return gameOfThree((number-1)/3)
    else:
        print(str(int(number)) + " + 1")
        return gameOfThree((number+1)/3)


if __name__ == '__main__':
    main()
