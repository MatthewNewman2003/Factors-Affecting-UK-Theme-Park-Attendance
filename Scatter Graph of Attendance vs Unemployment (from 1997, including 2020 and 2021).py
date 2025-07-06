import matplotlib.pyplot as plt
import pandas as pd

Data = pd.read_csv("Combined Merlin Park Attendance from 1997.csv")

print(Data.head())

Attendance = Data["Overall Attendance"]
Unemployment = Data["Annual UK Unemployment Rate (%)"]

plt.scatter(Unemployment, Attendance)
plt.xlabel("Annual Unemployment Rate (%)")
plt.ylabel("Combined Attendance (millions)")
plt.show()

AttendanceUnemploymentCorrelation = Attendance.corr(Unemployment)

print("The correlation coefficient between Attendance and Unemployment is:",AttendanceUnemploymentCorrelation)
