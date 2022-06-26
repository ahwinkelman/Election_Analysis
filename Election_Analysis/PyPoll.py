# The Data we need to retrieve

import csv
import os
#Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")

#Assign a variable for the file to load and the path
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Open the election results and read the file.
with open(file_to_load) as election_data:

#to do: read and analyze data here

#Read the file object with the reader function file to load is the variable assign to locate csv data, we opened file_to load and declared as election_date
    file_reader = csv.reader(election_data)

    #read and print the header row.
    headers= next(file_reader)
    print(headers)

#close the file
election_data.close()

# Use the open() function with the "w" mode we will write data to the file
with open(file_to_save, "w") as txt_file:

#write some data to the file
    #txt_file.write("Hello World")

#Write 3 counities to election alanysis.txt
    txt_file.write("Counties in the Election\n----------------\nArapahoe\nDenver\nJefferson")


#close the file
    txt_file.close()


# 1.the total # of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total numbe of votes each candidate won
# 5. The winner of the election based on popular vote