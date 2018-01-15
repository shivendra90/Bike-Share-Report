#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 14:31:57 2017

@author: Shiv
"""

""" Readiing in csv files."""
import csv
import pprint


def print_first_point(filename):
    city = filename.split('-')[0].split('/')[-1]
    print('\nCity: {}'.format(city))
    
    with open(filename, 'r') as csvfile:
        trip_reader = csv.DictReader(csvfile)
                
        first_trip = next(trip_reader)
        pprint.pprint(first_trip)
    return (city, first_trip)

datafiles = ['Washington-CapitalBikeshare-2016.csv', 'Bay-Area-Y3-trip-data.csv']

example_trips = {}
for data_file in datafiles:
    city, first_trip = print_first_point(data_file)
    example_trips[city] = first_trip
