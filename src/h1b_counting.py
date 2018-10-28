#!/usr/bin/env python3
''' '''
import os
import csv
import re

yearly_headers = {
    '2017': ['CASE_STATUS', 'SOC_CODE', 'WORKSITE_STATE'],
    '2016': ['CASE_STATUS', 'SOC_NAME', 'WORKSITE_STATE'],
    '2015': ['CASE_STATUS', 'SOC_NAME', 'WORKSITE_STATE'],
    '2014': ['STATUS', 'LCA_CASE_SOC_NAME', 'LCA_CASE_WORKLOC1_STATE'],
    '2013': ['STATUS', 'LCA_CASE_SOC_NAME', 'LCA_CASE_WORKLOC1_STATE'],
    '2012': ['STATUS', 'LCA_CASE_SOC_NAME', 'LCA_CASE_WORKLOC1_STATE'],
    '2011': ['STATUS', 'LCA_CASE_SOC_NAME', 'LCA_CASE_WORKLOC1_STATE'],
    '2010': ['STATUS', 'LCA_CASE_SOC_NAME', 'WORK_LOCATION_STATE1'],
    '2009': ['STATUS', 'LCA_CASE_SOC_NAME', 'LCA_CASE_WORKLOC1_STATE'],
    '2008': ['APPROVAL_STATUS', 'OCCUPATIONAL_TITLE', 'STATE_2']
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
        year = re.findall('\d{4}', a_file)
        if year:
            year = year[0]            
            print('year------->', year)
        else:
            year = '2017'
 
        with open(a_file, 'r') as fd:
            reader = csv.reader(fd, delimiter=';')
            header = next(reader)
           
            year_header = yearly_headers[year]
            arr = []
            for index in range(len(header)):
                if header[index] in year_header:
                    arr.append(index)

            print(header)
            count = 0
            for line in reader:
                print('----', line[arr[0]], '----', line[arr[1]], '----', line[arr[2]])
                count += 1
                if count == 10:
                    break
                #print(line[24], line[-3], line[2])

        print('=================== END ===================')

if __name__ == '__main__':
    # Open a file and get json object back
    file_name = 'h1b_input.csv'
    json = get_json(file_name)
