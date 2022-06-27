# Election_Analysis
## 1.Overview of Election Audit: 
The purpose of this election audit was to provide a detail overview of a congressional election with the following information: total number of votes, break down of votes by county, break down of votes by canididate, and election results


## 2.Election-Audit Results: 
-How many votes were cast in this congressional election?
369,711

A for loop was used to count a new vote each time it advanced to the new row. 1 row of data = 1 vote
    'For each row in the CSV file.
    for row in reader:
        # Add to the total vote count
        total_votes = total_votes + 1

-Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.
![County_results](https://user-images.githubusercontent.com/107078763/176033837-e2b01891-6ec6-43f5-9e5c-7948fa2b6e2e.png)
I created a variable of county_options as a list and county_votes as a dictionary.  I audited each line to append or add a new county name to the county_options variable if it was not in the list.  I added 1 vote to the county_votes dictionary if the row included the county option. I used a for loop to audit every row of code and to count the votes by county.

if county_name not in county_options:

            # 4b: Add the existing county to the list of counties.
            county_options.append(county_name)


            # 4c: Begin tracking the county's vote count.
            county_votes[county_name] =0
        


        # 5: Add a vote to that county's vote count.
        county_votes[county_name] +=1

-Which county had the largest number of votes?
Refer to the image above, Denver had the largest number of votes.

-Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.

![candidate bd](https://user-images.githubusercontent.com/107078763/176034024-b7d83714-3149-4a53-aa37-483f7102c840.png)
I created a variable of candidate_options as a list and candidate_votes as a dictionary.  I audited each line to append or add a new county name to the candidate_options variable if it was not in the list.  I added 1 vote to the candidate_votes dictionary if the row included the county option. I used a for loop to audit every row of code and to count the votes by county.

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

-Which candidate won the election, what was their vote count, and what was their percentage of the total votes?
![winner bd](https://user-images.githubusercontent.com/107078763/176034161-cc8db69f-d77f-486e-8bd5-b3bdc3913559.png)

## 3.Election-Audit Summary: In a summary statement, provide a business proposal to the election commission on how this script can be used—with some modifications—for any election. Give at least two examples of how this script can be modified to be used for other elections.
This code can be used for a different election audit as long as the csv file is formatted the same.  The CSV could be used for different counties or candidates. This code could be used for the same election the following year regardless of if there are more or less candidates or counties are added.  This code is versistile because it loops though each line of code and stores new candidates or counties in lists and will add votes to the dictionary regardless of the number of candidates/counties.
One other way this script could be modified is it could compare the voter turnout vs the total eligibile population of voters if that number was provided.  We could break down by county the voter turnout to try and focus campaign efforts for future elections to focus efforts on which areas need attention to get more voters.
