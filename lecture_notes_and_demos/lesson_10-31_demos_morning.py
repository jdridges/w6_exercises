movies = [
    ('The minions', 'X-Men First Class', 'Kicking and Screaming'),
    ('Her', 'Fall Guy', 'Prometheus'),
    ('Spiderman: Far from Home', 'Despicable Me 2', 'Freedom Writers')
    ]




        #CHANGING TUPLES TO LISTS TO MAKE CHANGES 
        
m1, m2, m3 = movies
change_m1 = list(m1)

change_m1.append('The Last Unicorn')

# print(change_m1)

m1 = tuple(change_m1)

movies[0] = m1

# print(movies)

change_m2 = list(m2)

change_m2[1] = 'The Fall guy'

m2 = tuple(change_m2)

movies[1] = m2

print(movies)







# print(f'I\'ve heard {movies[1][2]} is a good movie')

# for x in movies:
#     for i in x:
#         print(f'{i} is a good movie')       #for tuples in a list


# set4= movies[0]
# set5 = movies[1]
# set6 = movies[2]
# print(set4)

# movie1, movie2, movie3 = set4
# print(movie3)
# print(movies[0][2])