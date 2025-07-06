import matplotlib.pyplot as plt
import pandas as pd

Data = pd.read_csv("Combined Merlin Park Attendance from 1997 (excluding 2020 and 2021).csv")

print(Data.head())

Attendance = Data["Overall Attendance"]
Sunshine = Data["Average England Hours of Bright Sunshine April-October"]

plt.scatter(Sunshine, Attendance)
plt.xlabel("Average Number of Hours of Bright Sunshine")
plt.ylabel("Combined Attendance (millions)")
plt.show()

AttendanceSunshineCorrelation = Attendance.corr(Sunshine)

print("The correlation coefficient between Attendance and Sunshine is:",AttendanceSunshineCorrelation)
