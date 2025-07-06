import matplotlib.pyplot as plt
import pandas as pd

Data = pd.read_csv("Combined Merlin Park Attendance from 1997.csv")

print(Data.head())

Attendance = Data["Overall Attendance"]
Rainfall = Data["Average UK Rainfall April-October (mm)"]

plt.scatter(Rainfall, Attendance)
plt.show()

AttendanceRainfallCorrelation = Attendance.corr(Rainfall)

print("The correlation coefficient between Attendance and Rainfall is:",AttendanceRainfallCorrelation)
