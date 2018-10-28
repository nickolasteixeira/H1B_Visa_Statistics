#!/usr/bin/env python3
''' '''
import os
import csv

yearly_headers = {
    '2017': [{'CASE_STATUS':'Certified'}, 'SOC_CODE', 'WORKSITE_STATE'],
    '2016': 'WORKSITE_STATE',
    '2015': 'WORKSITE_STATE',
    '2014': 'WORKSITE_LOCATION_STATE',
    '2013': 'ALIEN_WORK_STATE',
    '2012': 'ALIEN_WORK_STATE',
    '2011': 'LCA_CASE_WORKLOC1_STATE',
    '2010': 'ALIEN_WORK_STATE',
    '2009': 'Alien_Work_State',
    '2008': 'Alien_Work_State'
}

def get_json(file_path):
    
    d = os.getcwd()
    d = os.chdir('input')
    all_files = os.listdir(d)
    
    csv_files = []
    for a_file in all_files:
        if a_file.endswith('.csv'):
            csv_files.append(a_file)

    print(csv_files)

    for a_file in csv_files:
        print(a_file)
        with open(file_path, 'r') as fd:
            reader = csv.reader(fd, delimiter=';')
            for line in reader:
                print(line[24])
                print(line[-3])
                print(line[2])
if __name__ == '__main__':
    # Open a file and get json object back
    file_name = 'h1b_input.csv'
    json = get_json(file_name)
