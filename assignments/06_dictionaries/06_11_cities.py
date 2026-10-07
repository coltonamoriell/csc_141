'''
Colton Amoriell
i under stand it 8/10
chapter 6 assignment 11



'''
cities = {
    'tokyo': {
        'country': 'japan',
        'population': 13_960_000,
        'fact': 'it is the most populous metropolitan area in the world.',
    },
    'paris': {
        'country': 'france',
        'population': 2_161_000,
        'fact': 'it is often called the City of Light.',
    },
    'santiago': {
        'country': 'chile',
        'population': 6_310_000,
        'fact': 'it is surrounded by the Andes mountains.',
    },
}

for city, city_info in cities.items():
    country = city_info['country'].title()
    population = city_info['population']
    fact = city_info['fact'].capitalize()

    print(f"\nCity: {city.title()}")
    print(f"\tCountry: {country}")
    print(f"\tPopulation: {population:,}")
    print(f"\tFact: {fact}")