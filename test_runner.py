#sys.path.append(/usr/local/lib/python3.9/site-packages)

import speedtest
from datetime import datetime
import csv

#Python server certificate validation
import os, ssl
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
getattr(ssl, '_create_unverified_context', None)):
	ssl._create_default_https_context = ssl._create_unverified_context


dt = datetime.now()

current_time = dt.strftime("%Y%m%d%H%M")
current_log = str("./output/wifi_results_"+current_time+".csv")

st = speedtest.Speedtest(secure=True)

results = []

print("Download: " + str(st.download()))
results.append(str(st.download()))

#Additional force float formatting option, not required
#'%.08f' % x

print("")

print("Upload: " + str(st.upload()))
results.append(str(st.upload()))

print("")

print("Ping: " + str(st.results.ping)) 
results.append(str(st.results.ping))

print("Creating results file < "+current_log+" > ..")
f = open(current_log, 'w')
writer = csv.writer(f)
writer.writerow(["Download","Upload","Ping"])
writer.writerow(results)

f.close()
