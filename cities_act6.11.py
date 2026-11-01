cities = {
    "jakarta": {
        "country": "indonesia",
        "population": 10500000,
        "fact": "Jakarta used to be called Batavia.",
    },
    "tokyo": {
        "country": "japan",
        "population": 14000000,
        "fact": "Tokyo used to be called Edo.",
    },
    "paris": {
        "country": "france",
        "population": 2100000,
        "fact": "Paris is home to the Louvre museum.",
    },
}

for city, info in cities.items():
    print(f"\n{city.title()}")
    print(f"  Country: {info['country'].title()}")
    print(f"  Population: about {info['population']:,}")
    print(f"  Fact: {info['fact']}")