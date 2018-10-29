#!/usr/bin/env python3
''' '''
import csv
import heapq
import operator
import os
from operator import itemgetter
import re
import sys

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

    ''' 
    d = os.getcwd()
    d = os.chdir('input')
    all_files = os.listdir(d)
    
    csv_files = []
    for a_file in all_files:
        if a_file.endswith('.csv'):
            csv_files.append(a_file)

    print(csv_files)
    # Store obj for each file
    output_file = []
 
    '''
    
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
        
                if certified:
                    profession = line[columns[1]]
                    state = line[columns[2]]
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

            from operator import itemgetter
            sorted_states = sorted(top_results['state'].items(), key=itemgetter(0))
            sorted_states = sorted(sorted_states, key=itemgetter(1))
            sorted_states = sorted(sorted_states, key=itemgetter(1), reverse=True)
            
            sorted_professions = sorted(top_results['profession'].items(), key=itemgetter(0))
            sorted_professions = sorted(sorted_professions, key=itemgetter(1))
            sorted_professions = sorted(sorted_professions, key=itemgetter(1), reverse=True)
        
        print(';'.join(top_results['header']))
        total = sorted_professions[0][1]
        for profession in sorted_professions[1:]:
             print("{};{};{:.1f}%".format(profession[0], profession[1], profession[1] / total * 100))
        print()
        print(';'.join(top_results['header']))
        for state in sorted_states[1:]:
            print("{};{};{:.1f}%".format(state[0], state[1], state[1] / total * 100))
            
        #output_file.append(output_obj)

def check_parameters(params):
    try:
        condition = True 
        if len(params) is not 4:
            print("Usage: Python3 <python.py script> <input_src.csv file> <occupations.txt file> <state.txt file>") 
            condition = False
        if not params[0].endswith('.py'):
            print("Usage: Script needs to be a Python file ending in '.py'")
            condition = False
        if not params[1].endswith('.csv'):
            print("Usage: Input source needs to be a Comma Separated File ending in '.csv'")
            condition = False
        if not params[2].endswith('.txt'):
            print("Usage: Output file occupation needs to be text files ending with '.txt'")
            condition = False
        if not params[3].endswith('.txt'):
            print("Usage: Output file state  needs to be text files ending with '.txt'")
            condition = False
        return condition
    except Exception as e:
        return False
        print(e)


def find_year(input_file):
    if not input_file:
        print("Please input a file to find the year of the file")
        return None

    year = re.findall('\d{4}', input_file)
    if year:
        year = year[0]            
        return year
    return '2017' 

def open_file(file_path, file_name, yearly_header):
    if not file_path:
        print("Please input a file path to change to")
        return None
    if not file_name:
        print("Please input a file to extract from")
        return None
    if not yearly_header:
        print("Please input a list of header attributes as strings")
        return None

    owd = os.getcwd()       
    os.chdir(file_path)
    certified_profession, certified_state = {}, {}
    with open(file_name, 'r') as fd:
        reader = csv.reader(fd, delimiter=';')
        file_header = next(reader)
        columns = [index for index in range(len(file_header)) if file_header[index] in yearly_header]
       
        for line in reader:
            certified = line[columns[0]] == "CERTIFIED"
            if certified:
                profession = line[columns[1]]
                state = line[columns[2]]
                if profession in certified_profession: certified_profession[profession] += 1
                elif profession not in certified_profession: certified_profession[profession] = 1
                
                if state in certified_state: certified_state[state] += 1
                elif state not in certified_state: certified_state[state] = 1

        
    return certified_profession, certified_state
    os.chir(owd)
        

   
def sort_dictionaries(occupations, states, amount):
    # Finds the top amount of occupations and states in a list
    top_occupations_list = heapq.nlargest(amount, occupations, key=occupations.get)
    top_states_list = heapq.nlargest(amount, states, key=states.get)

    # creates a new dictionary based on the top amount of occupations and states
    top_occupations = {occupation :occupations[occupation] for occupation in occupations}
    top_states = {state:states[state] for state in states}
    
    #sorts based on incrementing value, then alphabetical order
    sorted_occupations = sorted(top_occupations.items(), key=itemgetter(0))
    sorted_occupations = sorted(sorted_occupations, key=itemgetter(1))
    sorted_occupations = sorted(sorted_occupations, key=itemgetter(1), reverse=True)
    
    sorted_states = sorted(top_states.items(), key=itemgetter(0))
    sorted_states = sorted(sorted_states, key=itemgetter(1))
    sorted_states = sorted(sorted_states, key=itemgetter(1), reverse=True)
    
    return sorted_occupations, sorted_states
 
if __name__ == '__main__':
    # Open a file and get json object back
    if check_parameters(sys.argv):
        input_filepath =  sys.argv[1].rsplit('/', 1)[0]
        input_file = sys.argv[1].split('/')[-1]

        occ_filepath =  sys.argv[2].rsplit('/', 1)[0]
        occ_file = sys.argv[1].split('/')[-1]

        state_filepath = sys.argv[3].rsplit('/', 1)[0]
        state_file_name = sys.argv[3].split('/')[-1]

        # Finds the header that associates with each file based on the year -> Specs: https://www.foreignlaborcert.doleta.gov/performancedata.cfm        
        year = find_year(input_file)
        header = yearly_headers[year]
        
        certified_occupations, certified_states = open_file(input_filepath, input_file, header)
        #sort each object based on specifications
        sort1, sort2 = sort_dictionaries(certified_occupations, certified_states, 10)  
        
        # pass sorted values to write to output file
        
