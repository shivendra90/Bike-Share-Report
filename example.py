#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 14:23:25 2018

@author: Shiv
"""
import csv
import statistics as st

subs_data = []
cust_data = []

def dominant_season_for_users(file):
    
    # Define dictionary.
    with open(file, 'r') as csvfile:
        
        trip_reader = csv.DictReader(csvfile)
        
        for row in trip_reader:
            if row['user_type'] == 'Subscriber':
                subs_data.append(row['month'])
            elif row['user_type'] == 'Customer':
                cust_data.append(row['month'])
            else:
                'Not a valid user.'
                
        subs_mode = st.mode(subs_data)
        cust_mode = st.mode(cust_data)
                
        return(subs_mode, cust_mode)