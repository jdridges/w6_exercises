#doubler variable
doubler = lambda n: n * 2


#printing doubler using 8, -4, 'banana' 

print(doubler(8))
#returns 16 (as expected)

print(doubler(-4))
#returns -8(as expected)

print(doubler('banana'))
#returns bananabanana - prints the string twice (*2)

#tripler variable
tripler = lambda n: n *3

print(tripler(8))
print(tripler(-4))
print(tripler('banana'))


def multiplier(multiplier_value):
    return lambda n: n * multiplier_value
quadrupler = multiplier(4)
quintupler = multiplier(5)
sextupler = multiplier(6)
septupler = multiplier(7)
octupler = multiplier(8)
nonupler = multiplier(9)
decupler = multiplier(10)

print(f'The number 8 multiplied by 4 is {quadrupler(8)}')
print(f'-4 multiplied by 5 is {quintupler(-4)}')
print(f'The word banana sextupled is {sextupler('banana')}')
print(f'8 septupled is {septupler(8)}')
print(f'-4 octupled is {octupler(-4)}')
print(f'The word banana nonupled is {nonupler('banana')}')
print(f'8 decupled is {decupler(8)}')