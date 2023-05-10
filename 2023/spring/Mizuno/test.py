import pandas as pd
from scipy import stats

import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("2023/spring/Mizuno/sweets-temp.csv", encoding="JIS X 0208")

pd.plotting.scatter_matrix(df, figsize=(8, 8))
plt.show()

sns.parplot(df)
plt.show()
