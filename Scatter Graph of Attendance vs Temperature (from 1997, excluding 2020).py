import matplotlib.pyplot as plt
import pandas as pd

Data = pd.read_csv("Combined Merlin Park Attendance from 1997 (excluding 2020).csv")

print(Data.head())

Attendance = Data["Overall Attendance"]
Temperature = Data["Average England Max Temperature April-October (degrees C)"]

plt.scatter(Temperature, Attendance)
plt.xlabel("Average Maximum Temperature (degrees Celsius)")
plt.ylabel("Combined Attendance (millions)")
plt.show()

AttendanceTemperatureCorrelation = Attendance.corr(Temperature)

print("The correlation coefficient between Attendance and Temperature is:",AttendanceTemperatureCorrelation)
