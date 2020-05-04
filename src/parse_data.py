import json


class Airport:
    def __init__(self, airport_id, name, city, country, IATA, ICIAO, latitude, longitude, altitude, timezone, dst, tz,
                 station_type, source):
        self.airport_id = airport_id
        self.name = name
        self.city = city
        self.country = country
        self.IATA = IATA
        self.ICIAO = ICIAO
        self.latitude = latitude
        self.longitude = longitude
        self.altitude = altitude
        self.timezone = timezone
        self.dst = dst
        self.tz = tz
        self.station_type = station_type
        self.source = source

    def __str__(self) -> str:
        return f'{self.name} in {self.city}, {self.country}'


# airports = open("Airports.txt", "r", encoding="utf8")
# data = airports.readline()

data = []

with open('Airports.txt', "r", encoding="utf8") as airports:
    for line in airports:
        attributes = line.replace('"', "").split(",")
        airport = Airport(attributes[0], attributes[1], attributes[2], attributes[3], attributes[4], attributes[5],
                          attributes[6], attributes[7], attributes[8], attributes[9], attributes[10], attributes[11], attributes[12],
                          attributes[13])

        data.append(airport)

for el in data:
    if el.country == "Congo (Kinshasa)":
        print(el)

