# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 23:12:52 2019

@author: mengh
"""

from astropy.utils.data import download_file
from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt

year = "2019"
folder = "133" # throw folder into a loop - for folder in range(len(folders))
fname ="NEOS_SCI_2019133041551.fits"
base_url = "ftp://ftp.asc-csa.gc.ca/users/OpenData_DonneesOuvertes/pub/NEOSSAT/ASTRO/"
image_file_1 = download_file(base_url + '2019/133/NEOS_SCI_2019133041551.fits')

hdu = fits.open(image_file_1)
hdu.info()
hdu[0].header

hdu[0].header['JPOS2_1'] # X
hdu[0].header['JPOS2_2'] # Y
hdu[0].header['JPOS2_3'] # Z

#%%
image_data_1 = hdu[0].data
print(type(image_data_1))
print(image_data_1.shape)
RawVolt_1 = hdu[1].data

ACS_History_1 = hdu[2].data

'''
 Attitude Control System (ACS)
 (-0.131125, '16 - FINE_POINT', '85 - OPEN', 0.93560696, 0.23001328, -0.26094922, 0.060323898, -6.1442245e-07, -5.1281575e-07, -6.3954195e-07)
 Time from exposure start (s)
 Attitude control state ()
 Shutter state
 Estimated q0 (s) 
 Estimated q1 (s)
 Estimated q2 (s)
 Estimated q3 (s)
 Estimated w0 (s)
 Estimated w1 (s)
 Estimated w2 (s)

JPOS1_1 =           -3789.8776 / J2000 Position at Exp start, X-component (km)  
JPOS1_2 =            2496.9636 / J2000 Position at Exp start, Y-component (km)  
JPOS1_3 =           -5551.2474 / J2000 Position at Exp start, Z-component (km) 

JPOS2_1 =           -3747.5000 / J2000 Position at Exp middle, X-component (km) 
JPOS2_2 =            2484.5916 / J2000 Position at Exp middle, Y-component (km) 
JPOS2_3 =           -5585.4644 / J2000 Position at Exp middle, Z-component (km)

JPOS3_1 =           -3704.8988 / J2000 Position at Exp end, X-component (km)    
JPOS3_2 =            2472.0701 / J2000 Position at Exp end, Y-component (km)    
JPOS3_3 =           -5619.3443 / J2000 Position at Exp end, Z-component (km)   

POINTING	CMD	Commanded spacecraft pointing (Celestial Coordinates).
ELA min/maxk	Earth limb angle.
Vel_nnn	Velocity around X/Y/Z.
Roll / Avg / Dec_VEL	Roll, Avg, Declination velocity @ midpoint of exposure.
'''

Image_RD_1 = hdu[3].data
CCD_History_1 = hdu[4].data # 
RawTlm_1 = hdu[5].data # Raw Telemetry
#image_data = fits.getdata(image_file)
#plt.figure(figsize=(15, 15))
#plt.imshow(image_data,cmap = 'gray',vmin=1587,vmax = 3000)
#plt.colorbar()
#NBINS = 1000
#histogram = plt.hist(image_data.flatten(),NBINS)

#hdu_list[0].header['DATE']

Params = [None]*10
Params[1] = 'abs'
Params[0] = '20190101'










