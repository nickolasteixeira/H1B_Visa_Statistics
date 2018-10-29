#!/usr/bin/env python3
''' '''
import os
import csv
import re
import heapq
import operator

yearly_headers = {
    '2017': ['CASE_STATUS', 'SOC_NAME', 'WORKSITE_STATE'],
    '2016': ['CASE_STATUS', 'SOC_NAME', 'WORKSITE_STATE'],
    '2015': ['CASE_STATUS', 'SOC_NAME', 'WORKSITE_STATE'],
    '2014': ['STATUS', 'LCA_CASE_SOC_NAME', 'LCA_CASE_WORKLOC1_STATE'],
    '2013': ['STATUS', 'LCA_CASE_SOC_NAME', 'LCA_CASE_WORKLOC1_STATE'],
    '2012': ['STATUS', 'LCA_CASE_SOC_NAME', 'LCA_CASE_WORKLOC1_STATE'],
    '2011': ['STATUS', 'LCA_CASE_SOC_NAME', 'LCA_CASE_WORKLOC1_STATE'],
    '2010': ['STATUS', 'LCA_CASE_SOC_NAME', 'WORK_LOCATION_STATE2'],
    '2009': ['STATUS', 'LCA_CASE_SOC_NAME', 'LCA_CASE_WORKLOC1_STATE'],
    '2008': ['APPROVAL_STATUS', 'OCCUPATIONAL_TITLE', 'STATE_2']
}

def get_json(file_path):
    
    d = os.getcwd()
    d = os.chdir('input')
    all_files = os.listdir(d)
    
    csv_files = []
    for a_file in all_files:
        if a_file.endswith('input.csv'):
            csv_files.append(a_file)

    print(csv_files)
    # Store obj for each file
    output_file = []
 
    for a_file in csv_files:
        print(a_file)
        year = re.findall('\d{4}', a_file)
        if year:
            year = year[0]            
            print('year------->', year)
        else:
            year = '2017'

        output_obj = {year: {}}        

        with open(a_file, 'r') as fd:
            reader = csv.reader(fd, delimiter=';')
            header = next(reader)
           
            year_header = yearly_headers[year]
            columns = [index for index in range(len(header)) if header[index] in year_header]
            
            results_profession = {}
            results_state = {}
            count_profession, count_state = 0, 0
 
            #no_prof, no_state = 0, 0
            for line in reader:
                certified = line[columns[0]] == "CERTIFIED"
                profession = line[columns[1]]
                state = line[columns[2]]
        
                if certified and profession and state:
                    count_profession += 1
                    count_state += 1
                    if profession in results_profession:
                        results_profession[profession] += 1
                    elif profession not in results_profession:
                        results_profession[profession] = 1
                    if state in results_state:
                        results_state[state] += 1
                    elif state not in results_state:
                        results_state[state] = 1

                #if not profession and certified:
                 #   no_prof += 1                
                #if not state and certified:
                 #   no_state += 1

            #print('No profession -> {} No state -> {}'.format(no_prof, no_state))
            top_states = heapq.nlargest(10, results_state, key=results_state.get)
            top_professions = heapq.nlargest(10, results_profession, key=results_profession.get)

            top_results = {
                'header': ['TOP_OCCUPATIONS', 'NUMBER_CERTIFIED_APPLICATIONS', 'PERCENTAGE'],
                'profession': {profession: results_profession[profession] for profession in top_professions},
                'state': {state: results_state[state] for state in top_states}
            }
            top_results['profession']['total'] = count_profession
            top_results['state']['total'] = count_state
            
            
            output_obj[year] = top_results

            from functools import cmp_to_key
            print
            sorted_states = sorted(top_results['state'].items(), key=lambda k: k[1])
            print(sorted_states)
            sorted_states = sorted(top_results['state'].items(), key=lambda k: k[0], reverse=True)
            print(sorted_states)
            sorted_professions = sorted(top_results['profession'].items(), key=lambda k: (k[0], k[1]), reverse=True)
        
        print(';'.join(top_results['header']))
        total = sorted_professions[-1][1]
        for profession in sorted_professions:
             print("{};{};{:.1f}%".format(profession[0], profession[1], profession[1] / total * 100))
        print()
        print(';'.join(top_results['header']))
        for state in sorted_states:
            print("{};{};{:.1f}%".format(state[0], state[1], state[1] / total * 100))
            
        #output_file.append(output_obj)
    print(output_file)    

if __name__ == '__main__':
    # Open a file and get json object back
    file_name = 'h1b_input.csv'
    json = get_json(file_name)