#!/bin/bash
# Use this to run the script on the sample h1b_input.csv
#python3 ./src/h1b_counting.py ./input/h1b_input.csv ./output/top_10_occupations.txt ./output/top_10_states.txt

# I downloaded all the files from https://www.foreignlaborcert.doleta.gov/performancedata.cfm and listed them into my host folder. Unfortunately I was not able to host the large csv files onto github, so I had to figure a workout. Since I'm testing my application code in a Vagrant box, I had to download the files locally on my host and then vagrant scp them into my box. I could then test the files on my vagrant box
# If you do have the additional files (ex: files provided from the link you posted on the github readme of the challenge link: https://drive.google.com/drive/folders/1Nti6ClUfibsXSQw5PUIWfVGSIrpuwyxf, feel free to uncomment out the lines below to test the code

# To run multiple files in the input folder uncomment files below
#python3 ./src/h1b_counting.py ./input/H1B_FY_2014.csv ./output/top_10_occupations.txt ./output/top_10_states.txt
#python3 ./src/h1b_counting.py ./input/H1B_FY_2015.csv ./output/top_10_occupations.txt ./output/top_10_states.txt
python3 ./src/h1b_counting.py ./input/H1B_FY_2016.csv ./output/top_10_occupations.txt ./output/top_10_states.txt


# I also downloaded the rest of the years from https://www.foreignlaborcert.doleta.gov/performancedata.cfm
# If you have those files locally, feel free to uncommment the script and run the tests
#python3 ./src/h1b_counting.py ./input/H1B_FY_2013.csv ./output/top_10_occupations.txt ./output/top_10_states.txt
#python3 ./src/h1b_counting.py ./input/H1B_FY_2012.csv ./output/top_10_occupations.txt ./output/top_10_states.txt
#python3 ./src/h1b_counting.py ./input/H1B_FY_2011.csv ./output/top_10_occupations.txt ./output/top_10_states.txt
#python3 ./src/h1b_counting.py ./input/H1B_FY_2010.csv ./output/top_10_occupations.txt ./output/top_10_states.txt
#python3 ./src/h1b_counting.py ./input/H1B_FY_2009.csv ./output/top_10_occupations.txt ./output/top_10_states.txt
#python3 ./src/h1b_counting.py ./input/H1B_FY_2011.csv ./output/top_10_occupations.txt ./output/top_10_states.txt


# To cat out the results, uncomment below
#cat ./output/top_10_occupations.txt cat ./output/top_10_states.txt
