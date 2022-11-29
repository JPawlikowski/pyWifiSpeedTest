import os

from datetime import datetime
import numpy
import pandas as pd
from analysisGrapher import analysisGrapherFunc

import matplotlib.pyplot as plt

results_path = "./output/" 

downloads = []
uploads = []
pings = []
output_dates = []

#Note, need to make thi sort output files by date (ls -ltr)
for filename in os.listdir(results_path):
	f = os.path.join(results_path, filename)
	if os.path.isfile(f):
		#print(f)
		output_dates.append(f[22:26] + '-' + f[26:28])
		data = pd.read_csv(f)
		print(str(data.head()))
		downloads.append(data.loc[0].at['Download'] /  1000000)
		uploads.append(data.loc[0].at['Upload'] / 100000)
		pings.append(data.loc[0].at['Ping'])

#for val in downloads:
#	print(val)

#for i in output_dates:
	#print(i)

#Using 'x' later on for length of UPLOADS and PINGS lists
#Fine as long as all entry data has records for 3 fields (len(downloads)==len(uploads)==len(pings)
x = list(range(0,len(downloads)))

dt = datetime.now()
current_time = dt.strftime("%Y%m%d%H%M")

analysisGrapherFunc(output_dates, downloads, 'downloads', current_time)

analysisGrapherFunc(output_dates, uploads, 'uploads', current_time)

analysisGrapherFunc(output_dates, pings, 'pings', current_time)

