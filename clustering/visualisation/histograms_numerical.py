import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

csvfile = "../io/phoenix.event.csv"

df = pd.read_csv(csvfile)
df.hist()
plt.show()
