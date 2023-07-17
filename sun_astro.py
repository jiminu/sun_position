from astropy.coordinates import solar_system_ephemeris, get_body
from astropy.time import Time
import astropy.units as u
import math
import numpy as np

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
time = '2023-07-14T12:00:00'
time = Time.now()
# time = Time(time)

jd = time.jd

# Set the solar system ephemeris
solar_system_ephemeris.set("jpl")

# Get the Sun's coordinates in the ECI frame
sun = get_body("sun", time)

# Print the Sun's coordinates
x_gcrs, y_gcrs, z_gcrs = calc_xyz(sun.gcrs.ra.value, sun.gcrs.dec.value)
x_icrs, y_icrs, z_icrs = calc_xyz(sun.icrs.ra.value, sun.icrs.dec.value)
x_tete, y_tete, z_tete = calc_xyz(sun.tete.ra.value, sun.tete.dec.value)
x_cirs, y_cirs, z_cirs = calc_xyz(sun.cirs.ra.value, sun.cirs.dec.value)
x_fk5, y_fk5, z_fk5 = calc_xyz(sun.fk5.ra.value, sun.fk5.dec.value)

print('astropy gcrs')
print("Sun's X coordinate:", x_gcrs)
print("Sun's Y coordinate:", y_gcrs)
print("Sun's Z coordinate:", z_gcrs)
print('')

print('astropy icrs')
print("Sun's X coordinate:", x_icrs)
print("Sun's Y coordinate:", y_icrs)
print("Sun's Z coordinate:", z_icrs)
print('')

print('astropy tete')
print("Sun's X coordinate:", x_tete)
print("Sun's Y coordinate:", y_tete)
print("Sun's Z coordinate:", z_tete)
print('')

print('astropy cirs')
print("Sun's X coordinate:", x_cirs)
print("Sun's Y coordinate:", y_cirs)
print("Sun's Z coordinate:", z_cirs)
print('')

print('astropy fk5')
print("Sun's X coordinate:", x_fk5)
print("Sun's Y coordinate:", y_fk5)
print("Sun's Z coordinate:", z_fk5)
print('')

print('astropy itrs')
print("Sun's X coordinate:", sun.itrs.cartesian.x.value)
print("Sun's Y coordinate:", sun.itrs.cartesian.y.value)
print("Sun's Z coordinate:", sun.itrs.cartesian.z.value)
print('')

print('astropy teme')
print("Sun's X coordinate:", sun.teme.x)
print("Sun's Y coordinate:", sun.teme.y)
print("Sun's Z coordinate:", sun.teme.z)
print('')