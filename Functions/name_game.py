def trunc_name(name):
    name = name.lower()
    vowels = 'aeiou'

    if name[0] in vowels:
        print(name)
    elif len(name)>1 and name[1] in vowels:
        return name[1:]
    else: 
       return name [2:]
    
# print(name('Jacob'))
# print(name('CHARLIE'))

def name_game(name):
    full_name = name.lower()
    truncated = trunc_name(name)

    yield f'{full_name}, {full_name}, bo-b{truncated}'
    yield f'banana-fana fo-f{truncated}'
    yield f'me my-mo-m{truncated}'
    yield f'{full_name}!'

names_to_try = ['Jacob', 'carly', 'CHARLIE', 'Aidan', 'Braden', 'Billy Bob']

for name in names_to_try:
    print(f'Name game for {name}')
    for position in name_game(name):
        print(position)