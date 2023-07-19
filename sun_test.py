import math
import datetime
import numpy as np

def calculate_angle(x1, y1, z1, x2, y2, z2, x3, y3, z3):
    # 벡터 AB 계산
    AB_x = x2 - x1
    AB_y = y2 - y1
    AB_z = z2 - z1

    # 벡터 AC 계산
    AC_x = x3 - x1
    AC_y = y3 - y1
    AC_z = z3 - z1

    # AB와 AC의 내적 계산
    dot_product = AB_x * AC_x + AB_y * AC_y + AB_z * AC_z

    # 벡터의 크기 계산
    AB_length = math.sqrt(AB_x**2 + AB_y**2 + AB_z**2)
    AC_length = math.sqrt(AC_x**2 + AC_y**2 + AC_z**2)

    # 코사인 값 계산
    cos_theta = dot_product / (AB_length * AC_length)

    # 각도 계산 (라디안에서 도로 변환)
    angle = math.acos(cos_theta) * (180 / math.pi)

    return angle


def gcrs_to_cartesian(right_ascension, declination):
    # Convert right ascension and declination to radians
    right_ascension_rad = math.radians(right_ascension)
    declination_rad = math.radians(declination)

    # Calculate Cartesian coordinates
    x = math.cos(right_ascension_rad) * math.cos(declination_rad)
    y = math.sin(right_ascension_rad) * math.cos(declination_rad)
    z = math.sin(declination_rad)
    
    g = 357.5277233 + ((35999.05034 / 36525) * 2460139.5)
    a = 1.000140612 - (0.016708617 * np.cos(g * np.pi / 180)) - (0.000139589 * np.cos(2 * g * np.pi / 180))
    m = a * 149597870700
    x = m * x / 1000
    y = m * y / 1000
    z = m * z / 1000

    return x, y, z

def calculate_sun_position_gcrs(date_time):
    # Convert the date and time to Julian centuries since J2000.0
    reference_date = datetime.datetime(2000, 1, 1, 12, 0, 0)
    julian_centuries = (date_time - reference_date).total_seconds() / (86400 * 36525)

    # Mean longitude of the sun
    mean_longitude = (280.460 + 36000.770 * julian_centuries) % 360

    # Mean anomaly of the sun
    mean_anomaly = 357.529 + 35999.050 * julian_centuries

    # Ecliptic longitude
    ecliptic_longitude = (mean_longitude + 1.915 * math.sin(math.radians(mean_anomaly)) +
                          0.020 * math.sin(math.radians(2 * mean_anomaly))) % 360

    # Obliquity of the ecliptic
    obliquity = 23.439 - 0.013 * julian_centuries

    # Right ascension
    right_ascension = math.degrees(math.atan2(math.cos(math.radians(obliquity)) *
                                               math.sin(math.radians(ecliptic_longitude)),
                                               math.cos(math.radians(ecliptic_longitude))))

    # Declination
    declination = math.degrees(math.asin(math.sin(math.radians(obliquity)) *
                                         math.sin(math.radians(ecliptic_longitude))))

    return right_ascension, declination

# Example usage:
date_time = datetime.datetime(2023, 7, 14, 0, 0)  # Current UTC date and time

right_ascension, declination = calculate_sun_position_gcrs(date_time)

print("Right Ascension:", right_ascension)
print("Declination:", declination)

x, y, z = gcrs_to_cartesian(right_ascension, declination)

print(f'x: {x}\ny: {y}\nz: {z}')

angl = calculate_angle(0, 0, 0,
                       -54537787.29746191, 130248863.55205774, 56462268.18020495,
                       -54780063.70008579, 128670521.62751135, 55776561.186535895)

print(angl)