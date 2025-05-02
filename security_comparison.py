import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('../data/platform_metrics.csv')

# Plot Fraud Reduction
plt.figure(figsize=(8, 5))
plt.bar(df['Platform'], df['FraudReduction'], color='skyblue')
plt.title('Fraud Reduction by Blockchain Platform')
plt.ylabel('% Reduction in Fraud Cases')
plt.xlabel('Platform')
plt.grid(axis='y')
plt.tight_layout()
plt.savefig('../visuals/fraud_reduction.png')
plt.show()