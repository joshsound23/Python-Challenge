#import the OS Module
import os

#The module for reading csv files
import csv

csv_election = os.path.join('Resources', 'election_data.csv')

#create int to store votes
total_votes = 0
#create dict to store candidates and votes
candidate_votes = {}




with open (csv_election) as csv_file:
    csvreader = csv.reader(csv_file, delimiter=",")
    
  # Read the header row first 
    csv_header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:
        # add a vote for each new line
        total_votes +=1

        if row[2] not in candidate_votes.keys():
            #create new key with one vote
            candidate_votes[row [2]] = 1 
        else:
            candidate_votes[row[2]] += 1


#save the results to a text file
with open('analysis.txt', 'w') as output_file:

    print(f"Election Results")   

    print(f"total votes: {total_votes}")
    output_file.write(f"total votes: {total_votes}\n")

    highest_votes = 0
    #key is looping through the data and writing a value for a key 1 , key 2 and key 3.
    for key in candidate_votes.keys():
        percent = (candidate_votes[key]/total_votes) * 100
        print(f"{key}: {percent:.3f}% ({candidate_votes[key]})")
        output_file.write(f"{key}: {percent:.3f}% ({candidate_votes[key]})\n")
        #check if the current candidate has the most votes
        if candidate_votes[key] > highest_votes:
            winner = key
            highest_votes = candidate_votes[key]
    print(f"Winner: {winner}")
    output_file.write(f"Winner: {winner}")

    
