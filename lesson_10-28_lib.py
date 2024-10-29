import math
import statistics 
# gar_bill = [1.33, 4, 14.95, 2, 10, 29.98, 3.46]

# print(f' Total garbage bill is: $ {math.fsum(gar_bill)}') 
# print(f' Average line item amount is: ${statistics.mean(gar_bill)}')
# print(f'Median item amount: ${statistics.median(gar_bill)}')
# print(f'Mode of line items is: {statistics.mode(gar_bill)}')
# print(f'Bill sorted by amount: {sorted(gar_bill)}')


# python math Module and statistics Module in W3schools for more functions


                #Random module

# import random 

# gar_bill = [1.33, 4, 14.95, 2, 10, 29.98, 3.46]

# random.shuffle(gar_bill)
# print (gar_bill)

# print(random.sample(gar_bill, 2))

# print(random.choice(gar_bill))


                    #Datetime module

import datetime

now = (datetime.datetime.now())
print(now)
print(now.strftime("%A"))
