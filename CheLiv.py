import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('CheLiv.csv')

for name, df in df.groupby('Team'):
    plt.plot(df['Minute'], df['CumulativexG'], label=name, drawstyle='steps-post')

plt.legend()
plt.title('Chelsea vs Livepool xG')
plt.axis([0, max(df['Minute']), 0, 3])
plt.xticks(np.arange(0, max(df['Minute']), step=15))
plt.xlabel('Minutes Played')
plt.ylabel('Expected Goals')
plt.grid(True)
plt.show()
