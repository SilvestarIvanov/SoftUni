countries = input().split(", ")
city = input().split(", ")

countries_capitals = dict(zip(countries, city))
for country, city in countries_capitals.items():
    print(f"{country} -> {city}")