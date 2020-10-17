# Import dependencies
import os
import csv

# Path to collect data from the Resources folder
poll_data_csv_path = os.path.join('Resources', 'election_data.csv')

# Define function
def get_results(data):

    # Define variables
    totalVotesCount = 0
    votes = []
    candidateCount = []
    uniqueCandidates = []
    percent = []
     
    # Start looping through rows
    for row in data:

        # Count the total number of votes
        totalVotesCount += 1

        # Append unique names to the candidates list
        if row[2] not in uniqueCandidates:
            uniqueCandidates.append(row[2])

        # Make a list of all the votes
        votes.append(row[2])

    # Start a second loop that will populate the candidateCount with each vote
    for candidate in uniqueCandidates:
        candidateCount.append(votes.count(candidate))
        percent.append(round(votes.count(candidate)/totalVotesCount*100,3))

    # Find the winner using index position of the max count in candidateCount
    winner = uniqueCandidates[candidateCount.index(max(candidateCount))]
    
    # --> Print results to the terminal, use a loop for the number of uniqueCandidates
    print('Election Results')
    print('--------------------------------')
    print(f'Total Votes: {totalVotesCount}')
    print('--------------------------------')
    for i in range(len(uniqueCandidates)):
        print(f'{uniqueCandidates[i]}: {percent[i]}% {candidateCount[i]}')
    print('--------------------------------')
    print(f'Winner: {winner}')
    print('--------------------------------')

    # --> Export a text file with the results
    poll_file = os.path.join("Output", "Poll_Data.txt")
    with open(poll_file, "w") as outfile:

        outfile.write('Election Results')
        outfile.write('\n------------------------------------')
        outfile.write(f'\nTotal Votes: {totalVotesCount}')
        outfile.write('\n------------------------------------')
        for i in range (len(uniqueCandidates)):
            outfile.write(f'\n{uniqueCandidates[i]}: {percent[i]}% {candidateCount[i]}')
        outfile.write('\n------------------------------------')
        outfile.write(f'\nWinner: {winner}')
        outfile.write('\n------------------------------------')


# Open and read csv
with open(poll_data_csv_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first
    csv_header = next(csvfile)
    
    # use function
    get_results(csvreader)