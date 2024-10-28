            #find function

# sched1 = "Garbage pickup is Wednesday"
# sched2 = "Recycling pickup is Wednesday"
# sched3 = "Yard waste pickup is Friday"

# print(sched1.find('Garbage'))  #character G is not the same as g
# print(sched1.find('pickup'))
# print(sched1.find('Wednesday'))



# find searches left to right where rfind searches right to left. Rfind may be used when there are many characters.




                # format and .format functions

# inv_gar = 26
# inv_recy = 8
# inv_yw = 14

#this format function is more common 
# print(f'''Your total waste management bill is: 
#       ${format(inv_gar + inv_recy + inv_yw, ".2f")}''')

#   w3 schools is a good reference for formatting types. 
#   format function vs .format method

# total_bill = "Your total waste management bill is : ${total:.2f}"
# breakdown = "Total includes garbage ${0:.2f}, recycling ${1:.2f}, and yard waste ${2:.2f}".format(inv_gar, inv_recy, inv_yw)

#.format is less common but used to give a name for variables you may be finding out in the future. 
# print(total_bill.format(total = inv_gar + inv_recy + inv_yw))
# print(breakdown)



        # .replace function
# sched1 = "Garbage pickup is Wednesday"
# sched2 = "Recycling pickup is Wednesday"
# sched3 = "Yard waste pickup is Friday"

# print(f''' Schedule change! This week due to the holiday: 
#       {sched1.replace("Wednesday", "Thursday")}
#       {sched2.replace("Wednesday", "Thursday")}
#       {sched3.replace("Friday", "Saturday")}''')



            # range function
            # range (start, end, step)
            #start is option (starts at 0) and end is optional (starts at 1)
            # range(5) will give you output 1,2,3,4
test_range = range(1, 50, 5)
for x in test_range:
    print(x) 
