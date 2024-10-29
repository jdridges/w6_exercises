import random
        #using randint function between 2 and 11
print(random.randint(2,11))
        #using random function to extract random value from 0 to 1
print(random.random())

my_shopping_list = ['bananas', 'apples', 'granola', 'muffins', 'ice']

            #using choice function to choose a randomly selected value from list
print(random.choice(my_shopping_list))

            #using random.choices to assign weights to different items in the list and setting k = the number of total outputs (in list format)
print(random.choices(my_shopping_list, weights = [1,1,1,1,1], k = 10))

            #random sample is similar to random choices but without inclusion of duplicate values in the output
print(random.sample(my_shopping_list, k = 3))

            #random.shuffle shuffles the list and the output is the same list but shuffled randomly
random.shuffle(my_shopping_list)
print(my_shopping_list)