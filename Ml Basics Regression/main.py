import seaborn as sbn
import matplotlib.pyplot as plt

df = sbn.load_dataset('titanic')
df['Age_mean'] = df['age'].fillna(df['age'].mean())
print(df[['Age_mean','age']])
# sbn.displot(df['age'])
# plt.show()
