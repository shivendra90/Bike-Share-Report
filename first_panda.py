#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 18:55:09 2017

@author: Shiv
"""

""" This is a pandas csv reader file."""
import csv
import pandas as pd

def duration_in_mins(datum, city):
    datum = {}
    
    # Step 1. Define the csv tables.
    washington = pd.read_csv('Washington-CapitalBikeshare-2016.csv', sep = ',')
    bay_area = pd.read_csv('BayArea_Y3_trip_data.csv', sep = ',')
       
    # Step 2. Read in the csv file.
    if city == 'Bay Area':
        duration = float(bay_area(datum['Duration']))/60
    
    elif city == 'Washington':
        duration = float(washington(datum['Duration']))/60
        
    else:
        "Invalid city or datum."
        
    # Step 3. Extract only the 'Duration' column.
    return duration


    if city == 'Bay Area':
        durations = (bay_area['Duration'])/60
        for datum in durations:
            return duration[datum]
        
    elif city == 'Washington':
        durations = (washington['Duration'])/60
        for datum in durations:
            return duration[datum]
    
    else:
        "Invalid city or datum."
    