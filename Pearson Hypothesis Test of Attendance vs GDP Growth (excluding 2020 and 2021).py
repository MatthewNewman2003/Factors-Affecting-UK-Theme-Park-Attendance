import pandas as pd
from scipy.stats import pearsonr

Data = pd.read_csv("Combined Merlin Park Attendance from 1997 (excluding 2020 and 2021).csv")

Correlation, PValue = pearsonr(Data["Overall Attendance"], Data["Annual UK GDP Growth (%)"])

print("The Pearson correlation coefficient is",Correlation)
print("The p-value is:",PValue)

if 0.05 < PValue < 0.1:
    print("There is marginally significant evidence to reject the null hypothesis.")

elif 0.01 < PValue < 0.05:
    print("There is significant evidence to reject the null hypothesis.")

elif PValue < 0.01:
    print("There is extremely significant evidence to reject the null hypothesis.")

else:
    print("There is insufficient evidence to reject the null hypothesis.")
