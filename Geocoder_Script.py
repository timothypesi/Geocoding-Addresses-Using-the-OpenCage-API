# -*- coding: utf-8 -*-
"""
Created by Timothy Pesi.
"""

import pandas as pd
from opencage.geocoder import OpenCageGeocode

key = "Your Open Cage API goes"
geocoder = OpenCageGeocode(key)

addresses_df = pd.read_excel("C:\\Data\Addresses.xlsx") #   importing your dataset

addresses = addresses_df["Addresses"].values.tolist()

latitudes = [] #creating latitude attributes 
longitudes = [] #creating Longitude attributes

for address in addresses:
    result = geocoder.geocode(address,no_annotations="1") #geocoding the locations uing the geocode geocoder
    
    if result and len(result):
        longitude = result[0]["geometry"]["lng"]
        latitude = result[0]["geometry"]["lat"]
        
    else:
        longitude = "N/A"
        latitude = "N/A"
        
    latitudes.append(latitude)
    longitudes.append(longitude)
    

addresses_df["latitudes"] = latitudes
addresses_df["longitudes"] = longitudes

addresses_df.to_excel("Addresses_Geocoded.xlsx") #Exporting the dataset to location of choice