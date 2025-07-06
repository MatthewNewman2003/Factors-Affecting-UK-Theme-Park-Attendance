import matplotlib.pyplot as plt
import pandas as pd

Data = pd.read_csv("Combined Merlin Park Attendance from 1997.csv")

print(Data.head())

Attendance = Data["Overall Attendance"]
GDPGrowth = Data["Annual UK GDP Growth (%)"]

plt.scatter(GDPGrowth, Attendance)
plt.xlabel("Annual GDP Growth (%)")
plt.ylabel("Combined Attendance (millions)")
plt.show()

AttendanceGDPCorrelation = Attendance.corr(GDPGrowth)

print("The correlation coefficient between Attendance and GDP Growth is:",AttendanceGDPCorrelation)
