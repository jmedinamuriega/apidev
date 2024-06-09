import requests

def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets = response.json()['bodies']

    for planet in planets:
        if planet['isPlanet']:
            name = planet.get('englishName', 'Unknown')
            mass = planet.get('mass', {}).get('massValue', 'Unknown')
            orbit_period = planet.get('sideralOrbit', 'Unknown')
            print(f"Planet: {name}, Mass: {mass}, Orbit Period: {orbit_period} days")

fetch_planet_data()