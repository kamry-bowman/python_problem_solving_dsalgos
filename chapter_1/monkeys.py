from random import randrange


def imt():
    target =  "methinks it is like a weasel"
    length = len(target)
    score = 0
    counter = 0

    alph = [chr(x) for x in range(ord("a"), ord("z") + 1)]
    alph.append(" ")

    while (score < length and counter < 10000000):
        attempt = []

        while(len(attempt) < length):
            rand = randrange(len(alph))
            attempt.append(alph[rand])

        attemptScore = 0

        for i in range(len(attempt)):
            if attempt[i] == target[i]:
                attemptScore += 1
        
        if attemptScore > score:
            winner = ''.join(attempt)
            score = attemptScore
        counter += 1
    
    print(score)
    print(counter)
    return winner

print(imt())
