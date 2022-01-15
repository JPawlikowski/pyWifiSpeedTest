import os

#import sys
#sys.path.append('/usr/local/Cellar/python@3.9/3.9.8/bin/')

import numpy
import pandas as pd

import matplotlib.pyplot as plt

results_path = "./output/" 

downloads = []
uploads = []
pings = []

for filename in os.listdir(results_path):
	f = os.path.join(results_path, filename)
	if os.path.isfile(f):
		print(f)
		data = pd.read_csv(f)
		print(str(data.head()))
		downloads.append(data.loc[0].at['Download'])
		uploads.append(data.loc[0].at['Upload'])
		pings.append(data.loc[0].at['Ping'])

for val in downloads:
	print(val)

x = list(range(0,len(downloads)))
print(x)

plt.plot(x, downloads)

plt.savefig('./graphs/file1.png', dpi=None, facecolor='w', edgecolor='w', orientation='portrait', papertype=None, format=None, transparent=False, bbox_inches=None, pad_inches=0.1, frameon=None, metadata=None)

plt.show()


