import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../data/platform_metrics.csv')

# TPS Comparison
plt.figure(figsize=(8, 5))
plt.bar(df['Platform'], df['TPS'], color='orange')
plt.title('Transactions Per Second (TPS)')
plt.ylabel('TPS')
plt.xlabel('Platform')
plt.grid(axis='y')
plt.tight_layout()
plt.savefig('../visuals/tps_comparison.png')
plt.show()

# Uptime Comparison
plt.figure(figsize=(8, 5))
plt.bar(df['Platform'], df['Uptime'], color='green')
plt.title('System Uptime (%)')
plt.ylabel('Uptime %')
plt.xlabel('Platform')
plt.grid(axis='y')
plt.tight_layout()
plt.savefig('../visuals/uptime_comparison.png')
plt.show()

# Compliance Score
plt.figure(figsize=(8, 5))
plt.bar(df['Platform'], df['ComplianceScore'], color='purple')
plt.title('Compliance Score (0–10 Scale)')
plt.ylabel('Score')
plt.xlabel('Platform')
plt.grid(axis='y')
plt.tight_layout()
plt.savefig('../visuals/compliance_score.png')
plt.show()