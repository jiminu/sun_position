import spiceypy as spice
from datetime import datetime

# Load the SPICE kernels (you may need to download these kernels from the NAIF website)
path = '/home/jiminu/code/sun_position/data/'

spice.furnsh(f'{path}naif0012.tls')
spice.furnsh(f'{path}de430.bsp')
spice.furnsh(f'{path}pck00010.tpc')

# Specify the time of interest (in this example, it's the current time)
current_time = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')

et = spice.str2et(current_time)
# Define the observer and target as Earth and Sun, respectively
observer = 'EARTH'
target = 'SUN'

# Get the state (position and velocity) of the target relative to the observer
state, _ = spice.spkezr(target, et, 'J2000', 'NONE', observer)
state_IAU, _ = spice.spkgeo(10, et, 'IAU_EARTH', 399)

# Extract the position coordinates from the state
sun_position = state[:3]
sun_position_IAU = state_IAU[:3]

# Print the Sun's J2000 coordinates
print("spiceypy")
print(f"X: {sun_position[0]} km")
print(f"Y: {sun_position[1]} km")
print(f"Z: {sun_position[2]} km")

print("spiceypy IAU_EARTH")
print(f"X: {sun_position_IAU[0]} km")
print(f"Y: {sun_position_IAU[1]} km")
print(f"Z: {sun_position_IAU[2]} km")
# Unload the SPICE kernels

spice.unload(f'{path}naif0012.tls')
spice.unload(f'{path}de430.bsp')
spice.unload(f'{path}pck00010.tpc')