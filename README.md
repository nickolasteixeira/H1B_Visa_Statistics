# Insight Data Engineering Puzzle

## Problem

The problem for this solution was to parse through a file in a specific directory (input), look for specific attributes in that file (process that file) and based on the results, create a file in a specific directory (output). Input, processing and output is the basis of most problems in computer science.

## Approach
I didn't have much time to solve the problem because of other obligations, so I tried to brute force it with one function, then refactor into smaller, modular functions that do one thing. My approach was to get parse the argvs from the command line, find the paths of the input and output structure, find the input and output filenames, open the source file, parse through it, create data structures (ie: dictionaries) to hold the values I was looking for (ie: Occupations, number of certified occupations, and a total number of certified applications to find the percent values), then sort those values in descending order by value, then ascending by state with a specific length in mind, then pass those objects into separate write functions to write the data to a file.


I wanted to break the problem down into pieces. I wanted to separated the filepath, filename, year of the filename, specify the headers based on the file year, an object that stored all occurrences of occupations/states, count, and total number of certified applications so that if I had to change the structure of running the command, I could easily adjust the code in the statement `if __name__ == '__main_':`. 

1. I first get the filepath and filename for the inputs and output sources
2. I then find the year associated with that file to use the correct header (The header is important because I access information to build the data structure from the header, based on the year.
3. I then parse through the input file, build two dictionary objects with all the occupations/states occurences and the total amount
4. I then sort that dictionary to just find the top 10
5. I then write to files for both the occupations and states

## Run
To run the application:

- `$ git clone https://github.com/nickolasteixeira/DataEngineering_Puzzle_Insight'`
- `$ ./run`

If you have multiple input sources in your input folder, you can modify the `run.sh` script to use difference input and output sources. 
- **If you do modify the source, make sure the input filename has a year in the file name and is a csv file with the delimiter as ';'**
- **Ex: H1_FY_2015.csv** 

## Areas of Improvment

1. I could have definitely used branches for new features instead of pushing to master.
2. Always add more test cases
