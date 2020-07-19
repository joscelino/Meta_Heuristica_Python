# -*- coding: utf-8 -*-
# Importacao de bibliotecas
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Pre-processamento de dados
base = pd.read_csv('credit_data.csv')
base = base.dropna()
base.describe()

# Outlier na variavel idade usando Seaborn
sns.set(style="ticks", palette="pastel") #(style="whitegrid")
ax = sns.boxplot(x=base.iloc[:, 2], orient = "v")
outliers_age = base[(base.age< 18)]
plt.show()

# Outlier loan usando Matplotlib
plt.boxplot(base.iloc[:, 3])
plt.show()
outliers_loan = base[(base.loan > 13400)]