import random
def getSecretNum(numDigits):
    numbers = list(range(10))
    random.shuffle(numbers)
    secretNum = ''
    for i in range(numbers):
        secretNum += (numbers[i])
    print (secretNum)
getSecretNum(numDigits)