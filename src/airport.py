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

