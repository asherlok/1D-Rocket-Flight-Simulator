# IMPORT LIBRARIES
from math import pi
import numpy as np
import matplotlib.pyplot as plt

# DEFINE CONSTANTS
g=9.81          # In m/s^2
rho=1.225       # In kg/m^3

# INPUT ROCKET PARAMETERS AND MOTOR DETAILS
m=1             # In kg
diameter=0.08   # In m
Cd=0.5          # Unitless
T=30            # In N
burn_time=2     # In s

# CALCULATE S 
S=(pi*diameter**2)/4

# SET INTIAL CONDITIONS
time=0
height=0
velocity=0

# CALCULATE FORCES AND ACCELERATION
D=-(rho*velocity*abs(velocity)*S*Cd)/2
W=m*g
Net_Thrust=T-W+D
a=(T/m)-g-(rho*velocity*abs(velocity)*S*Cd)/(2*m)

print("Thrust=",T,"N")
print("Weight=",W,"N")
print("Drag=",D,"N")
print(f"Acceleration= {a:.2f} m/s^2")

# SEMI-IMPLICIT EULER
time_step=0.01
velocity_list=[velocity]
height_list=[height]
acceleration_list=[a]
time_list=[time]
while time <burn_time or velocity>0:
    if time<burn_time:
        thrust=T
    else:
        thrust=0

    D=-(rho*velocity*abs(velocity)*S*Cd)/2
    net_force=thrust-W+D
    a=net_force/m
    velocity=velocity+a*time_step
    height=height+velocity*time_step
    time=time+time_step
    velocity_list.append(velocity)
    height_list.append(height)
    time_list.append(time)
    acceleration_list.append(a)

print("--SIMULATION RESULTS--")
print(f"Apogee={height:.2f} m")
print(f"Time to Apogee={time:.2f} s")

# PLOT HEIGHT VS TIME AND VELOCITY VS TIME AND ACCELERATION VS TIME
time_array=np.array(time_list)
velocity_array=np.array(velocity_list)
height_array=np.array(height_list)
acceleration_array=np.array(acceleration_list)

plt.plot(time_array, height_array)
plt.title("Height vs Time")
plt.xlabel("Time (s)")
plt.ylabel("Height (m)")
plt.xlim(0)
plt.ylim(0)
plt.grid(True)
plt.show()

plt.plot(time_array, velocity_array)
plt.title("Velocity vs Time")
plt.xlabel("Time (s)")
plt.ylabel("Velocity (m/s)")
plt.xlim(0)
plt.ylim(0)
plt.grid(True)
plt.show()

plt.plot(time_array, acceleration_array)
plt.title("Acceleration vs Time")
plt.xlabel("Time (s)")
plt.ylabel("Acceleration (m/s^2)")
plt.xlim(0)
plt.grid(True)
plt.show()
