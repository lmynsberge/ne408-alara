#!/usr/bin/python

import csv

data = []
fluxes = []


datafile = open('adjflux','rb')
datareader = csv.reader(datafile, delimiter=' ', skipinitialspace=True)

datafileo = open('alara.adjflux_temp','wb')
datawriter = csv.writer(datafileo, delimiter=' ', quoting=csv.QUOTE_MINIMAL)

for row in datareader:
   data.append(row)

for i in range(len(data)):
   for j in range(len(data[i])):
      fluxes.append(data[i][j])

for k in range(0,len(fluxes),43):
   reversed = []
   for l in range(41,-1,-1):
      if k+l < len(fluxes):
         reversed.append(fluxes[k+l])
      elif k+l >= len(fluxes):
	     pass
   datawriter.writerow(reversed)
   datawriter.writerow('\n')





