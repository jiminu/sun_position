from astropy.coordinates import solar_system_ephemeris, get_body
from astropy.time import Time, TimeDelta
import astropy.units as u
import math
import numpy as np
import datetime

def datetime_to_julian(dt):
    a = (14 - dt.month) // 12
    y = dt.year + 4800 - a
    m = dt.month + 12 * a - 3

    julian_day = (
        dt.day + (153 * m + 2) // 5 + 365 * y + y // 4 - y // 100 + y // 400 - 32045
    )

    julian_date = julian_day + (dt.hour - 12) / 24.0 + dt.minute / 1440.0 + dt.second / 86400.0

    return julian_date

def calc_xyz(ra, dec, jd):
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

def save(positions, file_path):
    """ Create rectangle point list in 2d.

    Args:
        number (int): Number to make.
        file_path (string): *.txt file path.
    """
    num = 1
    f = open(file_path, 'w')
    for x, y, z in positions :
        f.write(f'{x}\t{y}\t{z}\n')
    f.close()


# Set the time for which you want to calculate the Sun's coordinates
solar_system_ephemeris.set("jpl")
time = Time('2023-07-14T00:00:00')
sun_positions = []


for i in range(86400):
    sun = get_body("sun", time)
    sun_positions.append([sun.teme.x.value, sun.teme.y.value, sun.teme.z.value])
    time = time + 1 * u.s
    
save(sun_positions, '/home/coop/mwji/three-filter/src/sun_pos_sec.txt')    


print('hello, world')