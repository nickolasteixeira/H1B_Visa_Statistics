#!/usr/bin/python3

#Each year, record header laytouts change. This is dictionary that mimics the header from each year. Refer to LCA Programs (H1-B, H-1B1, E-3) https://www.foreignlaborcert.doleta.gov/performancedata.cfm
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
