from astropy.coordinates import solar_system_ephemeris, get_body
from astropy.time import Time
import astropy.units as u

import sys

# def sun_propagation(startTime: str, timeLength: int, deltaT: int) -> list :
#     """calculate sun TEME cartesian positions.

#     Args:
#         startTime (str): 2000-01-01T00:00:00
#         timeLength (int): total time after start time. (seconds)
#         deltaT (int): time step (seconds) 

#     Returns:
#         list: [
#             [name, startTime, jd, deltaT],
#             [[x,y,z],[x,y,z]]
#         ]
#     """
#     deltaCheck = 0
#     time = Time(startTime)
#     jd = time.jd
#     solar_system_ephemeris.set("jpl")
    
#     result = [['sun', startTime, jd, deltaT], []]
#     for _ in range(timeLength // deltaT):
#         sun = get_body("sun", time)
#         result[-1].append([deltaCheck, sun.teme.x.value, sun.teme.y.value, sun.teme.z.value])
#         time = time + deltaT * u.s
#         deltaCheck = deltaCheck + deltaT
    
#     return result

def save(result, filePath):
    f = open(filePath, 'w')
    
    f.write(f'%name       : {result[0][0]}\n')
    f.write(f'%start time : {result[0][1]}\n')
    f.write(f'%julian time: {result[0][2]}\n')
    f.write(f'%delta (sec): {result[0][3]}\n')
    
    for delta, x, y, z in result[-1] :
        f.write(f'{delta}\t{x}\t{y}\t{z}\n')
    f.close()

def sun_propagation(year: int, month: int, day: int, hour: int, minute: int, sec: float,
                    timeLength: int, deltaT: int) -> list :
    """calculate sun TEME cartesian positions.

    Args:
        year (int): 2000
        month (int): 1
        day (int): 1
        hour (int): 1
        minute (int): 1
        sec (float): 1
        timeLength (int): total time after start time. (seconds)
        deltaT (int): time step (seconds) 


    Returns:
        list: [
            [name, startTime, jd, deltaT],
            [[x,y,z],[x,y,z]]
        ]
    """

    deltaCheck = 0
    startTime = f'{year}-{str(month).zfill(2)}-{str(day).zfill(2)}T{str(hour).zfill(2)}:{str(minute).zfill(2)}:{str(sec).zfill(2)}'
    time = Time(startTime)
    jd = time.jd
    solar_system_ephemeris.set("jpl")
    
    result = [['sun', startTime, jd, deltaT], []]
    for _ in range(timeLength // deltaT):
        sun = get_body("sun", time)
        result[-1].append([deltaCheck, sun.teme.x.value, sun.teme.y.value, sun.teme.z.value])
        time = time + deltaT * u.s
        deltaCheck = deltaCheck + deltaT
    
    return result


if __name__ == '__main__':
    args = sys.argv
    del args[0]
    
    year       = int(args[0])
    month      = int(args[1])
    day        = int(args[2])
    hour       = int(args[3])
    minute     = int(args[4])
    sec        = float(args[5])
    timeLength = int(args[6])
    deltaT     = int(args[7])
    savePath   = args[8]
    
    sunPropagations = sun_propagation(year, month, day, hour, minute, sec, timeLength, deltaT)
    save(sunPropagations, savePath)
    
    print('done')