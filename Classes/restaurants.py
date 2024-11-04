import datetime

class Restaurant:
    '''Stores name of Restaurant and types of food Restaurant supplies'''

    def __init__(self, rest_name, food_type):
        self.rest_name = rest_name
        self.food_type = food_type
    
    def describe_rest(self):
        print(f'{self.rest_name} serves {self.food_type}.')

    def rest_open(self):
        print(f'{self.rest_name} is open')
        

    
restaurant1 = Restaurant('Weedy\'s', 'American fast food')
restaurant2 = Restaurant('McNaldos', 'American fast food')
restaurant3 = Restaurant('Applebapple\'s', 'American fine dining')

restaurant1.describe_rest()
restaurant1.rest_open()
print()
restaurant2.describe_rest()
restaurant2.rest_open()
print()
restaurant3.describe_rest()
restaurant3.rest_open()


##### OR



# for x in [restaurant1, restaurant2, restaurant3]:
#     x.describe_rest()
#     x.rest_open()
#     print()