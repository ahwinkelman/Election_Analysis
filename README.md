# Election_Analysis
##1.Overview of Election Audit: 
The purpose of this election audit was to provide a detail overview of a congressional election with the following information: total number of votes, break down of votes by county, break down of votes by canididate, and election results


##2.Election-Audit Results: 
-How many votes were cast in this congressional election?
369,711

A for loop was used to count a new vote each time it advanced to the new row. 1 row of data = 1 vote
# For each row in the CSV file.
    for row in reader:
        # Add to the total vote count
        total_votes = total_votes + 1

Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.
![County_results](https://user-images.githubusercontent.com/107078763/176033837-e2b01891-6ec6-43f5-9e5c-7948fa2b6e2e.png)

Which county had the largest number of votes?
Refer to the image above, Denver had the largest number of votes.
Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.
Which candidate won the election, what was their vote count, and what was their percentage of the total votes?
##3.Election-Audit Summary: In a summary statement, provide a business proposal to the election commission on how this script can be used—with some modifications—for any election. Give at least two examples of how this script can be modified to be used for other elections.
