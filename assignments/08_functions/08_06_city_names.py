def city_country(city, country):
    """Return a string formatted as 'City, Country'."""
    return f"{city.title()}, {country.title()}"

# Call the function with three city-country pairs and print the returned values
print(city_country('santiago', 'chile'))
print(city_country('tokyo', 'japan'))
