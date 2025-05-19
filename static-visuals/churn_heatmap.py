import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('https://raw.githubusercontent.com/blastchar/telco-customer-churn/master/WA_Fn-UseC_-Telco-Customer-Churn.csv')
df = df.replace(' ', pd.NA).dropna()
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'])
numeric_cols = ['tenure', 'MonthlyCharges', 'TotalCharges']

corr = df[numeric_cols].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap: Churn-Related Features')
plt.tight_layout()
plt.savefig('churn_heatmap.png')
plt.show()
