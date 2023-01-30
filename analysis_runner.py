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

#Note, need to make this sort output files by date (ls -ltr)
for filename in os.listdir(results_path):
	f = os.path.join(results_path, filename)
	if os.path.isfile(f):
		#print(f)
		current_file_dttm_str = f[22:26] + '-' + f[26:28] + "-" + f[28:30] + " " + f[30:32] + ":" + f[32:34]
		current_file_dttm = datetime.strptime(current_file_dttm_str, '%Y-%m-%d %H:%M')
		output_dates.append(current_file_dttm)
		data = pd.read_csv(f)
		#print(str(data.head()))
		downloads.append(data.loc[0].at['Download'] /  1000000)
		uploads.append(data.loc[0].at['Upload'] / 1000000)
		pings.append(data.loc[0].at['Ping'])
"""
print('sorting...')

output_dates_sorted = output_dates.sort()
for i in output_dates:
	print(i)
"""

j = 0
change_made = False

#Sort manually by dates and accordingly suffle downloads/uploads/pings
#Consider adding a double check flow
while j in range(0, len(output_dates)):
	if output_dates[j] > output_dates[j+1]:
		date_to_switch = output_dates[j]
		#output_dates.remove(output_dates[j])
		output_dates.pop(j)
		output_dates.insert(j+1, date_to_switch)

		#switch also other lists
		download_to_switch = downloads[j]
		downloads.pop(j)
		downloads.insert(j+1, download_to_switch)

		upload_to_switch = uploads[j]
		uploads.pop(j)
		uploads.insert(j+1, upload_to_switch)

		ping_to_switch = pings[j]
		pings.pop(j)
		pings.insert(j+1, ping_to_switch)

		change_made = True
	else:
		print("sorted line skipped")
	if j == len(output_dates)-2: #at the bottom
		if change_made == True:
			change_made = False
			j = 0
			continue
		else:
			print("passed through with no changes - done")
			break
	else:
		j = j + 1
			

print("after manual sortation")
for i in output_dates:
	print(i)

#Using 'x' later on for length of UPLOADS and PINGS lists
#Fine as long as all entry data has records for 3 fields (len(downloads)==len(uploads)==len(pings)
x = list(range(0,len(downloads)))

dt = datetime.now()
current_time = dt.strftime("%Y%m%d%H%M")

analysisGrapherFunc(output_dates, downloads, 'downloads', current_time)

analysisGrapherFunc(output_dates, uploads, 'uploads', current_time)

analysisGrapherFunc(output_dates, pings, 'pings', current_time)

