def divide_by(num):
    try:
        div_num = int(num)
        if div_num == 0:
            raise ZeroDivisionError("Cannot be zero")           #raising an exception is creating an exception if problems may arise in the future (cannot divide a number by 0)
    except ValueError:
        print("Not a number")
        div_num = None      #assign none in order to have an output in the return statement
    except:
        print('Number cannot be zero')
        div_num = None
    return f'Your number is {div_num}'

print(divide_by(input('Enter a number: '))) #entering a string produces a ValueError, so add an except statement above
