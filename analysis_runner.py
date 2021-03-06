import os

#import sys
#sys.path.append('/usr/local/Cellar/python@3.9/3.9.8/bin/')

from datetime import datetime
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

#NOTE
#Using 'x' later on for length of UPLOADS and PINGS lists
#Fine as long as all entry data has records for 3 fields (len(downloads)==len(uploads)==len(pings)
x = list(range(0,len(downloads)))
#print(x)

dt = datetime.now()
current_time = dt.strftime("%Y%m%d%H%M")

#DOWNLOADS
current_file_downloads = str("./graphs/downloads_plot_"+current_time+".png")

plt.plot(x, downloads)

plt.savefig(current_file_downloads, dpi=None, facecolor='w', edgecolor='w', orientation='portrait', format=None, transparent=False, bbox_inches=None, pad_inches=0.1, frameon=None, metadata=None)

#plt.show()

#UPLAODS
current_file_uploads = str("./graphs/uploads_plot_"+current_time+".png")

plt.plot(x, uploads)

plt.savefig(current_file_uploads, dpi=None, facecolor='w', edgecolor='w', orientation='portrait', format=None, transparent=False, bbox_inches=None, pad_inches=0.1, frameon=None, metadata=None)

#plt.show()

#PINGS

current_file_pings = str("./graphs/ping_plot_"+current_time+".png")

plt.plot(x, pings)

plt.savefig(current_file_pings, dpi=None, facecolor='w', edgecolor='w', orientation='portrait', format=None, transparent=False, bbox_inches=None, pad_inches=0.1, frameon=None, metadata=None)

#plt.show()

