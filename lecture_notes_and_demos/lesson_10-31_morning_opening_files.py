# Open the file

f = open("survey_data.csv", 'x')
#x: Create file
#r: opens a file for reading
#a: opens a file for appending
#w:opens a file for writing



# Read the file 

print(f.readline(2000))
print(f.readlines(2000))

data = f.readlines()


#Close the file

f.close()




#manipulating the data:

data_list = []

for i in data:
    data_list.append(i.split(','))
