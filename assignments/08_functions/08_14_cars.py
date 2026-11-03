def make_car(manufacturer, model, **car_info):
    """Build a dictionary representing a car with arbitrary additional info."""
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    return car_info

# Call the function with required information and two extra key-value pairs
car = make_car('subaru', 'outback', color='blue', tow_package=True)

# Print the resulting dictionary
print(car)