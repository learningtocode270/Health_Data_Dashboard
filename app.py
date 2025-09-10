import pandas as pd
import matplotlib.pyplot as plt

data_file = "data/Prevalence_of_Selected_Measures_Among_Adults_Aged_20_and_Over__United_States__1999-2000_through_2017-2018.csv"
df = pd.read_csv(data_file)

# Look for hypertension rows
htn_df = (df[df['Measure'].str.contains('Hypertension', case=False, na=False)])
htn_df[['YearStart', 'YearEnd']] = htn_df['Survey Years'].str.split('-',expand=True)

#Convert to int
htn_df['YearStart'] = pd.to_numeric(htn_df['YearStart'], errors='coerce')
htn_df['YearEnd'] = pd.to_numeric(htn_df['YearEnd'], errors='coerce')

#Select relevant rows
htn_df = htn_df[['YearStart', 'YearEnd', 'Sex', 'Age Group', 'Percent', 'Measure']]

# Check unique measures to understand what we have
print("Unique measures:", htn_df['Measure'].unique())

#filter for male and female only
sex_df = htn_df[htn_df['Sex'].isin(['Male', 'Female'])]

#pivot so rows are years, columns are sex, values are prevalence
pivot_df = sex_df.pivot_table(
    index="YearEnd",
    columns='Sex',
    values='Percent',
    aggfunc='mean'
).reset_index()

print(pivot_df.head())

# Plot
plt.figure(figsize=(8,5))
plt.plot(pivot_df["YearEnd"], pivot_df["Male"], marker='o', label="Male")
plt.plot(pivot_df["YearEnd"], pivot_df["Female"], marker='o', label="Female")

plt.title("Hypertension Prevalence in U.S. Adults by Sex")
plt.xlabel("Year")
plt.ylabel("Prevalence (%)")
plt.legend()
plt.grid(True)
plt.show()