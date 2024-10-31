movies = [
    ('The minions', 'X-Men First Class', 'Kicking and Screaming'),
    ('Her', 'Fall Guy', 'Prometheus'),
    ('Spiderman: Far from Home', 'Despicable Me 2', 'Freedom Writers')
    ]

print(f'I\'ve heard {movies[1][2]} is a good movie')

for x in movies:
    for i in x:
        print(f'{i} is a good movie')       #for tuples in a list
        