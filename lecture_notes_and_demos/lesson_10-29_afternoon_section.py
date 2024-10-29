# current_time = '1:28 PM'
# time_result = None      #this is used as local variable. you can set it outside of the created function to redefine a variable


# def stopwatch(m, s):
#     # global time_result      # global variable allows you to keep the most recent time_result value (in this case, 0:48)
#     time_result = f'{m}:{s}'
#     return f' Time result is {time_result}'

# print(f'The current time is {current_time}')
# print(f'Result from stopwatch: {stopwatch(1, 12)}')
# print(f'Result from stopwatch: {stopwatch(0, 48)}')
# print(time_result)





                            # LAMBDA
# add_to_itself = lambda para1: para1 + para1
# print(add_to_itself(37))

# #This could be used also as a function

# def add_to_itself_fx(para2):
#     return para2 + para2
# print(add_to_itself_fx(22))


# calc_dict = {'plus': lambda n1, n2: n1 + n2,
#              'minus': lambda n1, n2: n1 - n2,
#              'times': lambda n1, n2: n1 *n2,
#              'divide': lambda n1, n2: n1 / n2
#              }
# print(calc_dict['divide'](24,2))
# print(calc_dict['times'](12,3))




# def discount_calculator(pct_off):
#     return lambda price: price * (1 - pct_off)

# discount20 = discount_calculator(.2)
# discount25 = discount_calculator(.25)

# price = float(input("Enter price: "))

# print(f'A 20% discount on {price} is {discount20(price)}')
# print(f'A 25% discount on {price} is {discount25(price)}')




                    #Generator function

# def caclulator(n1, n2):
#     return n1 + n2

# print(caclulator(34,25))

def calculator2(n1, n2):
    yield n1 + n2
    yield "Do you want to calculate another set of numbers?"
    y_n = input("Y or N").upper()
    yield f'You responded {y_n}'

for x in calculator2(19,9):
    print(x)