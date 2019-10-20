# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 23:12:52 2019

@author: mengh
"""

from astropy.utils.data import download_file
from astropy.io import fits
import numpy as np
from matplotlib.colors import LogNorm
import matplotlib.pyplot as plt

base_url = "ftp://ftp.asc-csa.gc.ca/users/OpenData_DonneesOuvertes/pub/NEOSSAT/ASTRO/"
year = "2019"
folder = "133"
file_name = "NEOS_SCI_2019133041551.fits"
image_file_1 = download_file(base_url+year+'/'+folder+'/'+file_name,cache = True)

time = file_name[9:22]
file_year = file_name[9:13]
file_day = file_name[13:16]
file_hr = file_name[16:18]
file_min = file_name[18:20]
file_sec = file_name[20:22]
hdu_list_1 = fits.open(image_file_1)
hdu_list_1.info()

#parameters(year, month, day, X, Y, Z)

Months = ['January','Feburary','March','April','May','June','July','August','September','October','November','December']
Days_1 = [31,29,31,30,31,30,31,31,30,31,30,31]
Days_2 = [31,28,31,30,31,30,31,31,30,31,30,31]

#Params = [None]*10
#Params[0] = file_year

if years % 4 == 0:
    for i in range(len(Months)):
        if sum(Days_1[0:i]) < days and days < sum(Days_1[0:i+1]):
            months = Months[i]
else:
    for i in range(len(Months)):
        if sum(Days_2[0:i]) < days and days < sum(Days_2[0:i+1]):
            months = Months[i]


#%% Final Parameters
            
day = int(file_day)
year = int(file_year)
month = months # string

x_coord = hdu[0].header['JPOS2_1'] # X
y_coord = hdu[0].header['JPOS2_2'] # Y
z_coord = hdu[0].header['JPOS2_3'] # Z

title = base_url+year+'/'+folder+'/'+file_name

#%% 

#get header key words
primary_hd = hdu_list_1[0].header
rawvolt_hd = hdu_list_1[1].header
ACS_History_hd = hdu_list_1[2].header
Image_RD_hd = hdu_list_1[3].header
ccd_history_hd = hdu_list_1[4].header
rawtlm_hd = hdu_list_1[5].header

#get data
image_data_1 = hdu_list_1[0].data
print(type(image_data_1))
print(image_data_1.shape)
RawVolt_1 = hdu_list_1[1].data
ACS_History_1 = hdu_list_1[2].data
Image_RD_1 = hdu_list_1[3].data
CCD_History_1 = hdu_list_1[4].data
RawTlm_1 = hdu_list_1[5].data
#image_data = fits.getdata(image_file)
#plt.figure(figsize=(15, 15))
#plt.imshow(image_data,cmap = 'gray',vmin=1587,vmax = 3000)
#plt.colorbar()
#NBINS = 1000
#histogram = plt.hist(image_data.flatten(),NBINS)

#hdu_list[0].header['DATE']


