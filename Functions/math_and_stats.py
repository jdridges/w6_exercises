import random 
import math
import statistics

vals1_100 = range(1,100)
vals_sample = random.sample(vals1_100, 75)
vals_choices = random.choices(vals1_100, k = 200)
radius = random.randint(3,10)
pi = math.pi

#sum of sample 75 samples from 1 to 100:
print(sum(vals_sample))
print('\n')

#avg of 75 sample values
mean_of_small_set = statistics.mean(vals_sample)
print((round(mean_of_small_set, 2)))
print('\n')


#median of 75 sample values
print(statistics.median(vals_sample))
print('\n')

#avg of 200 values
mean_of_large_set = statistics.mean(vals_choices)
print(round(mean_of_large_set,2))
print('\n')

#median of 200 values
print(statistics.median(vals_choices))
print('\n')

#mode of 200 values
print(statistics.mode(vals_choices))
print('\n')

#std dev of 200 values
std_dev =statistics.stdev(vals_choices)
print(round(std_dev, 2))
print('\n')

#variance of 200 values
variance_of_large_set= statistics.variance(vals_choices)
print(round(variance_of_large_set, 2))
print('\n')

#radius (rounded up)
radius_of_a_circle_up = math.ceil(radius * 2 * pi)
print(radius_of_a_circle_up)

#radius(rounded down)
radius_of_a_circle_down = math.floor(radius*2*pi)
print(radius_of_a_circle_down)