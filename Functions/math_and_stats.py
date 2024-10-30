import random 
import math
import statistics

vals1_100 = range(1,100)
vals_sample = random.sample(vals1_100, 75)
vals_choices = random.choices(vals1_100, k = 200)
radius = random.randint(3,10)
pi = math.pi

#sum of sample 75 samples from 1 to 100:
def sum_sample()

#avg of 75 sample values
print(statistics.mean(vals_sample))


#median of 75 sample values
print(statistics.median(vals_sample))

#avg of 200 values