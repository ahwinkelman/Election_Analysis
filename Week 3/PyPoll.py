# The Data we need to retrieve

import csv
import os
#Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")

#Assign a variable for the file to load and the path
file_to_save = os.path.join("analysis", "election_analysis.txt")

#1. Initialize a vote counter

total_votes = 0

#candidate options
candidate_options = []

#create candidate dictionary
candidate_votes = {}

#Winning Candidate and Winning count tracker
#Winning Criteria
winning_candidate = ""
winning_count= 0
winning_percentage = 0

#Open the election results and read the file.
with open(file_to_load) as election_data:

#to do: read and analyze data here

#Read the file object with the reader function file to load is the variable assign to locate csv data, we opened file_to load and declared as election_date
    file_reader = csv.reader(election_data)

    #read and print the header row.
    headers= next(file_reader)
    

    #print each row in the csv file/
    for row in file_reader:
        #print(row)

        #2. add to the total vote count
        total_votes += 1

        #Printe the candidate name from each row.
        candidate_name = row[2]

        #if candidate does not match existing candidate add the candidate name to the candidate list
        if candidate_name not in candidate_options:
            #add it to the list of candidates
            candidate_options.append(candidate_name)
            #2. begin tracking candidate's vote counts
            candidate_votes[candidate_name] = 0

        #Add a vote to candidate count
        candidate_votes[candidate_name] +=1 

 #save results to our text file
with open(file_to_save,"w") as txt_file:

    #Print the final vote count to the terminal
    election_results= (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
     #save the final vote count to the text file
    txt_file.write(election_results)
    #print the candidate vote dictionary
    #print(candidate_votes)

    #determine the percentage of votes for each candidate by looping through the counts
    #1. iterate through the candidate list
    for candidate_name in candidate_votes:
        #2. Retrieve vote count of candidate
        votes = candidate_votes[candidate_name]

        #3. Calculate the percentage of votes
        vote_percentage = float(votes) / float(total_votes) *100

        #4. Print candidate name and % of votes
        candidate_results =(f"{candidate_name}: received {vote_percentage:.1f}% of the vote")

        print(candidate_results)

        #Save candidate results to text file
        txt_file.write(candidate_results+"\n")



    #to do: print out each candidates name, vote count, and percentage of votes to the terminal
        #print(f"{candidate_name}:{vote_percentage:.1f}% ({votes:,})\n")

    #1. Determine if the votes are greather than the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
        #2. if true then set winning count = votes and winning percent =
        # vote percentage
            winning_count = votes
            winning_percentage = vote_percentage
            #3. Set the winning candidate = to candidate name
            winning_candidate = candidate_name

    #to do: print out the winning candidate, vote count and percentage to terminal
    winning_candidate_summary = (
        f"------------------------\n"
        f"Winner:{winning_candidate}\n"
        f"Winning Vote count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    #save the winning candidates name to text file
    txt_file.write(winning_candidate_summary)

    #print(f"{candidate_name}:{vote_percentage:.1f}% ({votes:,})\n")
    #printe the candidate list
    #print(candidate_options)

    #print total votes
    #print(total_votes)

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