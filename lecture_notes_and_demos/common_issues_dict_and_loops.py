characters = {
    'main' : 'Little Red Riding Hood',
    'villain' : 'Big Bad Wolf',
    'supporting' : 'Grandmother'
}

# for char in characters.values():
#     print(f'{char} is a character in the story')

# for char in characters.values():
#     counter = char += 1



# print(characters.keys())    #list of keys
# print(characters.values())  #list of values
# print(characters.items())   #tuples of key, value pairs

basket = {
    'pastries' : ('buns', 'bread', 'pie'),
    'medicines' : ('willow bark tea', 'elderberry cordial')
}

for i in basket.items():
    print(i)            # 2 tuples in our output

for i in basket.items():
    print(f'{characters["main"]}\'s basket items includes {i}')     #this will again return tuples

    for i in basket.items():
        goodies = ''
        for item in i[1]:
            if item == [1][-1]:
                goodies = goodies + 'and '
            goodies = goodies + item 
            if item != i[1][-1]:
                goodies = goodies + ', '
        print(f'{characters["main"]}\'s basket includes {i[0]} consisting of {goodies}')