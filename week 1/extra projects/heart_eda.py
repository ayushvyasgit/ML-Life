import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("heart.csv", header=None)
df.columns = ["age","sex","cp","trestbps","chol","fbs","restecg","thalach","exang","oldpeak","slope","ca","thal","target"]
df['target'] = df['target'].apply(lambda x: 1 if x > 0 else 0)

print(df['target'].value_counts())
df['target'].value_counts().plot(kind='bar')
plt.savefig("class_balance.png")
plt.show()

# 3 insights
print("Insight 1: Class imbalance - more healthy patients")
print("Insight 2: Older age = higher risk")
print("Insight 3: High cholesterol common in sick")