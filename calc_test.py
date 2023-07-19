from datetime import datetime, timedelta
import math
import numpy as np

def calc_xyz(ra, dec, jd):
    x = math.cos(math.radians(ra)) * math.cos(math.radians(dec))
    y = math.sin(math.radians(ra)) * math.cos(math.radians(dec))
    z = math.sin(math.radians(dec))
    
    g = 357.5277233 + ((35999.05034 / 36525) * 2460139.5)
    a = 1.000140612 - (0.016708617 * np.cos(g * np.pi / 180)) - (0.000139589 * np.cos(2 * g * np.pi / 180))
    m = a * 149597870700
    x = m * x / 1000
    y = m * y / 1000
    z = m * z / 1000
    
    return x, y, z

def julian_centuries(date):
    J2000 = datetime(2000, 1, 1, 12, 0, 0)
    centuries = (date - J2000).total_seconds() / (365.25 * 24 * 60 * 60 * 100)
    return centuries

def calculate_sun_position(date):
    centuries = julian_centuries(date)

    # Mean longitude of the Sun
    L = math.radians((280.460 + 0.9856474 * centuries) % 360)

    # Mean anomaly of the Sun
    g = math.radians((357.528 + 0.9856003 * centuries) % 360)

    # Ecliptic longitude of the Sun
    lambda_sun = math.radians(L + 1.915 * math.sin(g) + 0.02 * math.sin(2 * g))

    # Obliquity of the ecliptic
    epsilon = math.radians(23.439 - 0.0000004 * centuries)

    # Right ascension of the Sun
    alpha = math.atan2(math.cos(epsilon) * math.sin(lambda_sun), math.cos(lambda_sun))

    # Declination of the Sun
    delta = math.asin(math.sin(epsilon) * math.sin(lambda_sun))
    
    return calc_xyz(math.degrees(alpha), math.degrees(delta), centuries)

# Example usage
date = datetime(2023, 7, 14)
x, y, z = calculate_sun_position(date)
print(f"{x}\n{y}\n{z}")