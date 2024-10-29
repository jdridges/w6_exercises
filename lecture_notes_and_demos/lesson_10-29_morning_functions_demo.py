# def my_first_function():
#     print("Hello world!")
#     return "How are you?"

# my_first_function()     #this calls to function because print is included within function

# print(my_first_function())  #print statement calls to the full function, including the return value

#codewars is necessary for trying out functions







# def calculator(n1, n2, operation = '+'):
#     print(f'Input values are {n1} and {n2}')
#     print(f'You have chose the {operation} operation')
#     if operation == '-':
#         return n1 - n2
#     elif operation == '*':
#         return n1 * n2
#     elif operation == '/':
#         return n1 / n2
#     else:
#         return n1 + n2


# print(calculator(54, 111))    #if no parameters are given in print statement, else is defaulted to. (54,111, '*') will return multiplication of the numbers
# print(calculator(77,32, '-'))





   



                     #arbitrary- *args returns a tuple

# def caculator2(*nums):
#     return nums

# print(caculator2(2,4,6,8))


#return to page 27 to go over this again 

# def relative(name, relationship):
#     return f'{name} is my {relationship}'

# print(relative('Becky', 'cousin'))      #base level keyword arguments





             





                   #arbitrary keyword arguements- **kwargs returns a dictionary 

# def rels(rel,name, **kwargs):
#     kwargs['relationship'] = rel
#     kwargs['name'] = name
#     return kwargs

# person1 = rels('cousin', 'Becky', attribute = 'funny')
# print(person1)
# person2 = rels('uncle', 'Joe', nickname = 'Scooter')
# print(person2)




#best practice is to include a return statment in your functions
