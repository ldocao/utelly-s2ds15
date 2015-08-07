###PURPOSE: plot duration against imdbrating scatter plot

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

csvfile = "../io/phoenix.event.csv"

df = pd.read_csv(csvfile)


data = df[['||metadata||imdb||value','||metadata||duration', '||topic||type']]
data = data.replace(to_replace="TV",value=0.1)
data = data.replace(to_replace="Movie",value=1.)


plt.figure()
data.plot(kind='scatter', x='||metadata||duration', y='||metadata||imdb||value', c = "||topic||type");
plt.show()

