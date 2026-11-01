# Reviewed for PEP 8
def city_country(city, country):
    """Return a city and country in the format 'City, Country'."""
    return f"{city.title()}, {country.title()}"


print(city_country("santiago", "chile"))
print(city_country("jakarta", "indonesia"))
print(city_country("tokyo", "japan"))