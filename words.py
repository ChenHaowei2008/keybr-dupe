from random import choice
import time
times = []
for i in range(100000):
    startTime = time.time()
    vowels = ('a', 'e', 'i', 'o', 'u')
    consts = ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'qu', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z', 'tt', 'ch', 'sh')
    isVowel = False
    word = ''
    for i in range(5):
        if(isVowel): word += choice(vowels)
        else: word += choice(consts)
        isVowel = not isVowel
    times.append(time.time() - startTime)
print(sum(times)/len(times))