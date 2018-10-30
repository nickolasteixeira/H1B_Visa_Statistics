#!/usr/bin/env python3
'''Module that '''
import csv
import heapq
import os
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
    if not input_file or type(input_file) is not str:
        print("Please pass a string ojbect as an input to find the year of the file")
        return None

    year = re.findall('\d{4}', input_file)
    if year:
        year = year[0]            
        return year
    return '2017' 

def open_file(file_path, file_name, yearly_header):
    if not file_path or type(file_path) is not str:
        print("Please input a file path to change to as a string object")
        return None
    if not file_name or type(file_path) is not str:
        print("Please input a file to extract from as a string object")
        return None
    if not yearly_header or type(yearly_header) is not list:
        print("Please input a list of header attributes as a string object")
        return None
    
    owd = os.getcwd()       
    os.chdir(file_path)
    certified_occupation, certified_state = {}, {}
    with open(file_name, 'r') as fd:
        reader = csv.reader(fd, delimiter=';')
        file_header = next(reader)
        columns = [index for index in range(len(file_header)) if file_header[index] in yearly_header]

        #Keeping track of a total number to then get the percentages later for file output      
        total_certified_state, total_certified_occupation = 0, 0 
        for line in reader:
            certified = line[columns[0]] == "CERTIFIED"
            if certified:
                total_certified_state += 1
                total_certified_occupation += 1
                profession = line[columns[1]]
                state = line[columns[2]]
                if profession in certified_occupation: certified_occupation[profession] += 1
                elif profession not in certified_occupation: certified_occupation[profession] = 1
                
                if state in certified_state: certified_state[state] += 1
                elif state not in certified_state: certified_state[state] = 1

        #Adding the total count of certified profession and state to the dictionary to calcualte values
        certified_occupation['total'] = total_certified_occupation
        certified_state['total'] = total_certified_state
        
    os.chdir(owd)
    return certified_occupation, certified_state

   
def sort_dictionaries(occupations, states, amount=10):
    if not occupations or type(occupations) is not dict:
        print("No certified occupations to sort through")
        return None
    if not states or type(states) is not dict:
        print("No certified states to sort through")
        return None

    # Finds the top amount of occupations and states in a list
    top_occupations_list = heapq.nlargest(amount, occupations, key=occupations.get)
    top_states_list = heapq.nlargest(amount, states, key=states.get)

    # creates a new dictionary based on the top amount of occupations and states
    top_occupations = {occupation:occupations[occupation] for occupation in top_occupations_list}
    top_states = {state:states[state] for state in top_states_list}
   
    #sorts based on incrementing value, then alphabetical order
    sorted_occupations = sorted(top_occupations.items(), key=lambda x: (-x[1], x[0]))
    sorted_states = sorted(top_states.items(), key=lambda x: (-x[1], x[0]))
   
    return sorted_occupations, sorted_states

def write_occupation(occupations, file_path, file_name, header):
    if not occupations or type(occupations) is not list:
        print("No top occupations. Please provide occupations input as a list")
        return None
    if not file_path or (type(file_path) is not str or type(file_path) is not str):
        print("No file path or file name provided. Please provide both as a string object")
        return None
    if len(header) is not 3 or type(header) is not list or not header:
        print("No header. Please provide list of 3 header string values")
        return None

    owd = os.getcwd()       
    os.chdir(file_path)
    total = occupations[0][1]
    with open(file_name, 'w') as fd:
        title = "{};{};{}".format(header[0], header[1], header[1])
        fd.write("{}\n".format(title))
        for occ in occupations[1:]:
            string = "{};{};{:.1f}%".format(occ[0], occ[1], occ[1]/total * 100)
            fd.write("{}\n".format(string)) 
    os.chdir(owd)

def write_state(states, file_path, file_name, header):
    if not states or type(states) is not list:
        print("No top occupations. Please provide occupations input as a list")
        return None
    if not file_path or (type(file_path) is not str or type(file_path) is not str):
        print("No file path or file name provided. Please provide both as a string object")
        return None
    if len(header) is not 3 or type(header) is not list or not header:
        print("No header. Please provide list of 3 header string values")
        return None
        
    owd = os.getcwd()       
    os.chdir(file_path)
    total = states[0][1]
    with open(file_name, 'w') as fd:
        title = "{};{};{}".format(header[0], header[1], header[1])
        fd.write("{}\n".format(title))
        for state in states[1:]:
            string = "{};{};{:.1f}%".format(state[0], state[1], state[1]/total * 100)
            fd.write("{}\n".format(string)) 
    os.chdir(owd)

if __name__ == '__main__':
    # Open a file and get json object back
    if check_parameters(sys.argv):
        input_filepath =  sys.argv[1].rsplit('/', 1)[0]
        input_file = sys.argv[1].split('/')[-1]

        occ_filepath =  sys.argv[2].rsplit('/', 1)[0]
        occ_file = sys.argv[2].split('/')[-1]
        occ_header = ['TOP_OCCUPATIONS','NUMBER_CERTIFIED_APPLICATIONS', 'PERCENTAGE']

        state_filepath = sys.argv[3].rsplit('/', 1)[0]
        state_file = sys.argv[3].split('/')[-1]
        state_header = ['TOP_STATES', 'NUMBER_CERTIFIED_APPLICATIONS', 'PERCENTAGE']

        # Finds the header that associates with each file based on the year -> Specs: https://www.foreignlaborcert.doleta.gov/performancedata.cfm        
        year = find_year(input_file)
        header = yearly_headers[year]

        certified_occupations, certified_states = open_file(input_filepath, input_file, header)
        #sort each object based on specifications
        top_occupation, top_state = sort_dictionaries(certified_occupations, certified_states, 10)  

        # pass sorted values to write to output file
        write_occupation(top_occupation, occ_filepath, occ_file, occ_header)
        write_state(top_state, state_filepath, state_file, state_header)  
