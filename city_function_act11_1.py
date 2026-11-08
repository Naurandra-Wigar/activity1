def get_formatted_city_country(city, country, population=None):
    """Mengembalikan 'Kota, Negara' atau 'Kota, Negara - population xxx'."""
    city_country = f"{city}, {country}".title()
    if population:
        return f"{city_country} - population {population}"
    return city_country