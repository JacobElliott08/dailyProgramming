

def main():

    total = 1234567
    iterations = 0
    while(total > 9):
        total = sumNumber(total)
        iterations += 1

    print(iterations)


def sumNumber(n):
    remainingTotal = n
    total = 0
    digit = 0
    while (remainingTotal > 0):
        digit = int(remainingTotal % 10)
        remainingTotal = int(remainingTotal / 10)
        total += digit
    return total

if __name__ == "__main__":
    main()
