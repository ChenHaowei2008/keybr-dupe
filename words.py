import random 

vowels = ('a', 'e', 'i', 'o', 'u')
consts = ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'qu', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z', 'tt', 'ch', 'sh')
isVowel = False
length = 5
word = ''

for i in range(length):
    if(random.randint(1,100) > 38):
        word += random.choice(consts)
    else: 
        word += random.choice(vowels)
print(word)