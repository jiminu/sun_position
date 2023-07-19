from astropy.coordinates import solar_system_ephemeris, get_body
from astropy.time import Time
import astropy.units as u
import math
import numpy as np
from datetime import datetime

def datetime_to_julian(dt):
    a = (14 - dt.month) // 12
    y = dt.year + 4800 - a
    m = dt.month + 12 * a - 3

    julian_day = (
        dt.day + (153 * m + 2) // 5 + 365 * y + y // 4 - y // 100 + y // 400 - 32045
    )

    julian_date = julian_day + (dt.hour - 12) / 24.0 + dt.minute / 1440.0 + dt.second / 86400.0

    return julian_date

def calc_xyz(ra, dec):
    x = math.cos(math.radians(ra)) * math.cos(math.radians(dec))
    y = math.sin(math.radians(ra)) * math.cos(math.radians(dec))
    z = math.sin(math.radians(dec))
    
    g = 357.5277233 + ((35999.05034 / 36525) * jd)
    a = 1.000140612 - (0.016708617 * np.cos(g * np.pi / 180)) - (0.000139589 * np.cos(2 * g * np.pi / 180))
    m = a * 149597870700
    x = m * x / 1000
    y = m * y / 1000
    z = m * z / 1000
    
    return x, y, z

# Set the time for which you want to calculate the Sun's coordinates
time = '2023-07-14T00:00:00'

# utc
# time = Time.now()
# time = Time(datetime.now())
time = Time(time)


print(time)

jd = time.jd

# Set the solar system ephemeris
solar_system_ephemeris.set("jpl")

# Get the Sun's coordinates in the ECI frame
sun = get_body("sun", time)

print('astropy gcrs')
print("Sun's X coordinate:", sun.gcrs.cartesian.x)
print("Sun's Y coordinate:", sun.gcrs.cartesian.y)
print("Sun's Z coordinate:", sun.gcrs.cartesian.z)
print('')

print('astropy icrs')
print("Sun's X coordinate:", sun.icrs.cartesian.x)
print("Sun's Y coordinate:", sun.icrs.cartesian.y)
print("Sun's Z coordinate:", sun.icrs.cartesian.z)
print('')

print('astropy tete')
print("Sun's X coordinate:", sun.tete.cartesian.x)
print("Sun's Y coordinate:", sun.tete.cartesian.y)
print("Sun's Z coordinate:", sun.tete.cartesian.z)
print('')

print('astropy cirs')
print("Sun's X coordinate:", sun.cirs.cartesian.x)
print("Sun's Y coordinate:", sun.cirs.cartesian.y)
print("Sun's Z coordinate:", sun.cirs.cartesian.z)
print('')

print('astropy fk5')
print("Sun's X coordinate:", sun.fk5.cartesian.x)
print("Sun's Y coordinate:", sun.fk5.cartesian.y)
print("Sun's Z coordinate:", sun.fk5.cartesian.z)
print('')

print('astropy itrs')
print("Sun's X coordinate:", sun.itrs.cartesian.x)
print("Sun's Y coordinate:", sun.itrs.cartesian.y)
print("Sun's Z coordinate:", sun.itrs.cartesian.z)
print('')

print('astropy teme')
print("Sun's X coordinate:", sun.teme.x)
print("Sun's Y coordinate:", sun.teme.y)
print("Sun's Z coordinate:", sun.teme.z)
print('')