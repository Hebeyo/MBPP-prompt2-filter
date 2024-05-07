def wind_chill(v,t):
    windchill = 13.12 + 0.6215*t -  11.37*(v**0.16) + 0.3965*t*(v**0.16)
    return int(round(windchill, 0))
