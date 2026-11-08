from city_functions import get_formatted_city_country


def test_city_country():
    """Apakah 'Santiago, Chile' dihasilkan dengan benar?"""
    formatted = get_formatted_city_country("santiago", "chile")
    assert formatted == "Santiago, Chile"


def test_city_country_population():
    """Apakah 'Santiago, Chile - population 5000000' dihasilkan dengan benar?"""
    formatted = get_formatted_city_country("santiago", "chile", population=5000000)
    assert formatted == "Santiago, Chile - population 5000000"