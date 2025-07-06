import matplotlib.pyplot as plt
import pandas as pd

Data = pd.read_csv("Combined Merlin Park Attendance from 1997 (excluding 2020 and 2021).csv")

print(Data.head())

Attendance = Data["Overall Attendance"]
Inflation = Data["Annual UK CPI Inflation (%)"]

plt.scatter(Inflation, Attendance)
plt.xlabel("Annual CPI Inflation Rate (%)")
plt.ylabel("Combined Attendance (millions)")
plt.show()

AttendanceInflationCorrelation = Attendance.corr(Inflation)

print("The correlation coefficient between Attendance and CPI Inflation is:",AttendanceInflationCorrelation)
