#import csv
#f = open('Users/jorg62/Desktop/dash_price.csv', 'r')
#csv_f = csv_reader(f)

import os
import csv

candidates = []
number_votes = 0
vote_counts = []
election_data = ['1', '2']


for files in election_data:
    election_dataCSV = csvpath = os.path.join("election_data.csv")
    
    #Split the data with commas since that is your delimiter
    with open(election_dataCSV) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
            line = next(csvreader,None)
                # Using Nested For Loop
                for line in csvreader:
                    
                    #Establish vote count
                    number_votes = number_votes +1
                        
                        # Establish Candidate
                        candidate = line[2]
                            
                            # add votes
                            if candidate in candidates:
                                candidate_index = candidates.index(candidate)
                                    vote_counts[candidate_index] = vote_counts[candidate_index] + 1
                                        
                                        # new spot for candidate in the list
                                        else:
                                            candidates.append(candidate)
                                                vote_counts.append(1)

#Declare the other variables:
percentages = []
    max_votes = vote_counts[0]
    max_index = 0
    
    #Wpercentages and winner (in a For Loop)
    for count in range(len(candidates)):
        vote_percentage = vote_counts[count]/number_votes*100
        percentages.append(vote_percentage)
        if vote_counts[count] > max_votes:
            max_votes = vote_counts[count]
            print(max_votes)
            max_index = count
winner = candidates[max_index]
    
    percentages = [round(i,2) for i in percentages]
    
    # Summary  results
    print("Election Results")
    print("--------------------------")
    print(f"Total Votes: {number_votes}")
    print("--------------------------")
    for count in range(len(candidates)):
        print(f"{candidates[count]}: {percentages[count]}% ({vote_counts[count]})")
    print("--------------------------")
    print(f"Winner:  {winner}")
    print("--------------------------")

#Export file
output_file = election_dataCSV[0:-4]
    write_election_dataCSV = f"{output_file}pypoll_results.txt"
    filewriter = open(write_election_dataCSV, mode = 'w')
    
    # Write results 
    filewriter.write("Election Results\n")
    filewriter.write("-----------------------------\n")
    filewriter.write(f"Total Votes:  {number_votes}\n")
    filewriter.write("-----------------------------\n")
    for count in range(len(candidates)):
        filewriter.write(f"{candidates[count]}: {percentages[count]}% ({vote_counts[count]})\n")
filewriter.write("-----------------------------\n")
    filewriter.write(f"Winner:  {winner}\n")
    filewriter.write("-----------------------------\n")
    
    # Close the text file
    filewriter.close()
