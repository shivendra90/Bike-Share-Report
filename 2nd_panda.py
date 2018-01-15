#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 13:58:02 2017

@author: Shiv
"""
import pandas as pd

def duration_in_mins2(datum, city):
    washington = pd.read_csv('Washington-CapitalBikeshare-2016.csv', sep =',')
    bay_area = pd.read_csv('BayArea_Y3_trip_data.csv', sep = ',')
    
    if city == 'Bay Area':
        durations = (bay_area['Duration'])/60
        for datum in durations:
            duration = durations[datum]
            return duration
        
    elif city == 'Washington':
        durations = (washington['Duration'])/60
        for datum in durations:
            duration = durations[datum]
            return duration
    
    else:
        "Invalid city or datum."

