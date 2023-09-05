from astropy import units as u
from poliastro.bodies import Earth, Sun

from poliastro.twobody import Orbit

r = [-2.77880220000000e+07, -3.17067190000000e+07, 3.42128000000000e+05] * u.m
v = [2.31245200000000e+03, -2.02658000000000e+03, -2.47880000000000e+01] * u.m / u.s

orb = Orbit.from_vectors(Earth, r, v)

orb.plot()