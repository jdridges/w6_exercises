#Trying multiple names
name = 'John Doe'
#name = 'Grace Flores'
#name = 'JB Oinonen

space = name.find(' ')

first_name = name[:space]
last_name = name[space + 1:]


print(f'Full Name: {name}')
print(f'First Name: {first_name}')
print(f'Last Name: {last_name}')
