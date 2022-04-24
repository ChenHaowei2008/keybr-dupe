import random 
def generateWord(length, vowels, consts, vowelsWeight, constsWeight)
    #vowels = ('a', 'e', 'i', 'o', 'u')
    #vowelsWeight = (21.87, 34.67, 28.67, 20, 6.67)
    #consts = ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'tt', 'ch', 'sh', 'qu')
    word = ''

    for i in range(length):
        #38 percent of english characters are vowels
        #More accurate because yes.
        if(random.randint(1,100) > 38):
            word += ''.join(random.choices(consts, weights=constsWeight))
        else: 
            word += ''.join(random.choices(vowels, weights=vowelsWeight))
    return word