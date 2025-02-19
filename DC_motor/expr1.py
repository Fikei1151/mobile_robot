import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dc_motor = {"voltage": [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
            "period": [22.5, 14.3, 10.6, 8, 3.5, 3.05, 2.7, 2.1, 2.25, 2, 1.75]} 

rpm = []

for t in dc_motor['period']:
    rpm_wheel = 60/(t * 0.001 * 5 * 20)
    rpm.append(rpm_wheel)
dc_motor["rpm_wheel"] = rpm

current = []
for i in dc_motor["voltage"]:
    current.append(i)
dc_motor["current"] = current

df = pd.DataFrame(dc_motor)
print(df)

# voltage vs rpm
x = dc_motor['voltage']
y = dc_motor['rpm_wheel']

plt.plot(x, y)
plt.title("Voltage and RPM_wheel")
plt.xlabel('Voltage(V)')
plt.ylabel('RPM_wheel(RPM)')
plt.xticks(np.arange(2, 13, step=1))
plt.grid()
plt.show()

# voltage vs current
x = dc_motor['voltage']
y = dc_motor['current']

plt.plot(x, y)
plt.title("Voltage and Current")
plt.xlabel('Voltage(V)')
plt.ylabel('Current(A)')
plt.xticks(np.arange(2, 13, step=1))
plt.grid()
plt.show() 

# current vs rpm
x = dc_motor['current']
y = dc_motor['rpm_wheel']

plt.plot(x, y)
plt.title("Current and RPM_wheel")
plt.xlabel('Current(A)')
plt.ylabel('RPM_wheel(RPM)')
plt.xticks(np.arange(2, 13, step=1))
plt.grid()
plt.show()


