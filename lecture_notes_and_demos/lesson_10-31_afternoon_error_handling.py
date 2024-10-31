# try:        #code you want to run
#     age =  int(input("Please enter your age: "))
# except ValueError:          #adding potential error message
#     print("Invalid entry. Age must be a number.")
# else:               
#     print(f'Age provided is {age}')
# finally:                    #finally pops up regardless of an error or not
#     print("Thank you!")


#-----------------------------------------------


# try:
#     list = []
#     age = int(input("Please enter your age: "))
#     try:
#         list.append(age)
#         print(list[0])
#     except IndexError:
#         print("Cannot locate specified item")
# except ValueError:
#     print("Error detected. Please input only a number for age")
# else:
#     print(f'Agre provided is {age}')
# finally:
#     print("Thank you!")

#-----------------------------------------------

# try:
#     f = open('survey_data.csv')
#     data = f.read()
# except:
#     print("Error raised")
# else:
#     print("file input accepted")
# finally:
#     f.close()

# print(data[:100])


#--------------------------------------------

        #LOOPING TRY/EXCEPT BLOCKS
# print('# Division calculator # \n')

# first_n = None

# while first_n == None:
#     try:
#         first_n = float(input('First number: '))
#     except:
#         print('Invalid input. Please try again.')
#---------------------------------------------
# second_n = None
# answer = None

# while second_n == None:
#     try:
#         second_n = float(input('Second number: '))
#         answer = first_n/second_n
#     except:
#         print('Invalid input. Must be a non zero number')
#         second_n = None
#     else:
#         print(f'Your answer is {answer}')
        
# print("\n# Thank you for using the division calculator #")

#finally statement would not make sense in this loop as it prints regardless of the error

#------------------------------------------

#pass removes the response portion from except statement as shown below:

# while second_n == None:
#     try:
#         second_n = float(input('Second number: '))
#         answer = first_n/second_n
#     except:
#         pass
#         second_n = None
#     else:
#         print(f'Your answer is {answer}')


#----------------------------------------------
# try:
#     result = 90 / 0
# except ZeroDivisionError:
#     print("Cannot divide by zero")