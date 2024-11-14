# Display output of plots directly in Notebook
import sys
import os
import matplotlib.pyplot as plt
import fsspec
import fsspec.implementations.http as fshttp
from pelicanfs.core import PelicanFileSystem, PelicanMap, OSDFFileSystem
import time



def convert_to_speed(times,size):
    return [size/x for x in times]

def read_https(url, repeat=10):
    results = []
    print(url)
    for i in range(repeat):
        start = time.time()
        fh = fsspec.open(url)
        test = fh.open().read()
        end = time.time()
        results.append(end-start)
        print(i)

    return results



if len(sys.argv) > 1:
    file = sys.argv[1]
else:
    https_url = 'https://data.rda.ucar.edu/d083002/grib2/2016/2016.01/fnl_20160102_00_00.grib2' # ~ 17 MB
    https_url_200 = 'https://data.rda.ucar.edu/d131003/anl/anl_mean_1836_CAPE_sfc.nc'
    https_url_500 = 'https://data.rda.ucar.edu/d084001/2024/20241109/gfs.0p25.2024110900.f000.grib2' # ~ 500 MB
    osdf_url = https_url.replace('https://data.rda.ucar.edu/', 'osdf:///ncar/rda/')
    osdf_url_200 = https_url_200.replace('https://data.rda.ucar.edu/', 'osdf:///ncar/rda/')
    osdf_url_500 = https_url_500.replace('https://data.rda.ucar.edu/', 'osdf:///ncar/rda/')


print('http tests')
http_benchmark_20  = convert_to_speed(read_https(https_url), 17)
http_benchmark_200 = convert_to_speed(read_https(https_url_200), 260)
http_benchmark_500 = convert_to_speed(read_https(https_url_500), 500)

print('osdf tests')
osdf_benchmark_20  = convert_to_speed(read_https(osdf_url), 17)
osdf_benchmark_200 = convert_to_speed(read_https(osdf_url_200), 260)
osdf_benchmark_500 = convert_to_speed(read_https(osdf_url_500), 500)


reps = 11
osdf_500_first = []
for i in range(1,reps):
    new_url = osdf_url_500.replace('f000','f'+f'{i*3}'.zfill(3))
    print(new_url)
    start = time.time()
    osdf_file = fsspec.open(new_url)
    test = osdf_file.open().read()
    end = time.time()
    osdf_500_first.append(end-start)
    print(end-start)

osdf_500_first = convert_to_speed(osdf_500_first, 500)

reps = 11
osdf_200_first = []
for i in range(1836,1836+reps):
    new_url = osdf_url_200.replace('1837', f'{i}')
    print(new_url)
    start = time.time()
    osdf_file = fsspec.open(new_url)
    test = osdf_file.open().read()
    end = time.time()
    osdf_200_first.append(end-start)
    print(end-start)

osdf_500_first = convert_to_speed(osdf_500_first, 500)


reps = 12
osdf_20_first = []
for i in range(2,reps):
    new_url = osdf_url.replace('20160101','201601'+f'{i}'.zfill(2))
    print(new_url)
    start = time.time()
    osdf_file = fsspec.open(new_url)
    #test = osdf_file.open().read()
    end = time.time()
    osdf_20_first.append(end-start)

osdf_20_first = convert_to_speed(osdf_20_first, 17)


fig, ax = plt.subplots(figsize=(10, 6))
ax.set_title("Direct downloads from Madison")
ax.set_xticklabels(['HTTPS 20 MB','OSDF 20 MB - Cached', 'OSDF 20 MB - First Run'])
ax.set_ylabel('Speed (MB/s)')
ax.boxplot([http_benchmark_20,osdf_benchmark_20,osdf_20_first])
ax.plot()
fig.savefig('20.png')


fig, ax = plt.subplots(figsize=(10, 6))
ax.set_title("Direct downloads from Madison")
ax.set_xticklabels(['HTTPS 200 MB','OSDF 200 MB - Cached', 'OSDF 200 MB - First Run'])
ax.set_ylabel('Speed (MB/s)')
ax.boxplot([http_benchmark_200,osdf_benchmark_200,osdf_200_first])
ax.plot()
fig.savefig('200.png')


fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xticklabels(['HTTPS 500 MB','OSDF 500 MB - Cached','OSDF 500 MB - First Try'])
ax.set_ylabel('Speed (MB/s)')
ax.set_title("Direct downloads from Madison")
ax.boxplot([http_benchmark_500,osdf_benchmark_500,osdf_500_first])
ax.plot()
fig.savefig('500.png')

