def describe_city(city, country="Iceland"):
  """Print a sentence describing a city and its country."""
  print(f"{city} is in {country}.")


# 1. Using the default country (Iceland)
describe_city("Reykjavik")

# 2. Using the default country for another city
describe_city("Akureyri")

# 3. Providing a non-default country
describe_city("Tokyo", "Japan")