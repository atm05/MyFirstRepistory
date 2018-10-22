import sys
animals = { 'a': ['horse'], 'b': ['baboon'], 'c': ['giraffe']} 
animals['d'] = ['donkey'] 
animals['d'].append('dog') 
animals['d'].append('dingo')
def how_many(animals):
    count = 0
    for i in animals.keys():
        count += len(animals[i])
    return (count)
def biggest(animals):
    maxe = "a"
    for i in animals.keys():
        if len(animals[i]) >len(animals[maxe]):
            maxe =i
    return maxe
def dstats(animals):
    l=() 
    l= l +(how_many(animals),)
    l = l +(len(animals[biggest(animals)]),)
    return l
print(dstats(animals))

