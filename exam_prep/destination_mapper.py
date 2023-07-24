import re


def mark_valid_locations(string):
    pattern = r'(=|/)([A-Z][A-Za-z]{2,})\1'
    valid_locations = re.findall(pattern, string)
    destinations = [location[1] for location in valid_locations]
    travel_points = sum(len(location[1]) for location in valid_locations)

    print(f"Destinations: {', '.join(destinations)}")
    print(f"Travel Points: {travel_points if valid_locations else 0}")


string = input()
mark_valid_locations(string)

