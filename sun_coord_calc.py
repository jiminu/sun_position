import math
import datetime
import numpy as np

def calculate_sun_coordinates_eci():
    # Get the current date and time
    now = datetime.datetime(2023, 7, 14, 0, 0, 0)
    # now = datetime.datetime.now()
    print(f'time now : {now}')
    #NOTE: time now : 2023-07-14 16:17:55.99669455
    
    # Calculate the number of Julian centuries since J2000.0
    jd = 2451545.0 + (now - datetime.datetime(2000, 1, 1, 12, 0, 0)).total_seconds() / 86400.0
    print(f'total seconds : {(now - datetime.datetime(2000, 1, 1, 12, 0, 0)).total_seconds()}')
    #NOTE: total seconds : 742623505.682179
    
    t = (jd - 2451545.0) / 36525.0

    # Calculate the mean longitude of the Sun
    L = (280.46646 + 36000.76983 * t + 0.0003032 * t**2) % 360

    # Calculate the mean anomaly of the Sun
    M = (357.52911 + 35999.05029 * t - 0.0001537 * t**2) % 360

    # Calculate the ecliptic longitude of the Sun
    lambda_sun = L + 1.914602 * math.sin(math.radians(M)) + 0.019993 * math.sin(math.radians(2 * M))
    lambda_sun %= 360

    # Calculate the obliquity of the ecliptic
    epsilon = 23.439291 - 0.0130042 * t

    # Convert the ecliptic longitude and obliquity to radians
    lambda_rad = math.radians(lambda_sun)
    epsilon_rad = math.radians(epsilon)

    # Calculate the right ascension (RA)
    numer = math.cos(epsilon_rad) * math.sin(lambda_rad)
    denom = math.cos(lambda_rad)
    ra = math.degrees(math.atan2(numer, denom))
    ra %= 360

    # Calculate the declination (Dec)
    dec = math.degrees(math.asin(math.sin(epsilon_rad) * math.sin(lambda_rad)))

    # Convert spherical coordinates to Cartesian coordinates
    x = math.cos(math.radians(ra)) * math.cos(math.radians(dec))
    y = math.sin(math.radians(ra)) * math.cos(math.radians(dec))
    z = math.sin(math.radians(dec))

    g = 357.5277233 + ((35999.05034 / 36525) * jd)
    a = 1.000140612 - (0.016708617 * np.cos(g * np.pi / 180)) - (0.000139589 * np.cos(2 * g * np.pi / 180))
    m = a * 149597870700
    x = m * x / 1000
    y = m * y / 1000
    z = m * z / 1000
    
    #NOTE: output unit is kilometer

    return x, y, z

# Calculate the Sun's coordinates in the ECI frame
x, y, z = calculate_sun_coordinates_eci()

# Print the Sun's coordinates
print('calc')
print("Sun's X coordinate:", x)
print("Sun's Y coordinate:", y)
print("Sun's Z coordinate:", z)