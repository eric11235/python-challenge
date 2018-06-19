#Import CSV module and OS modules

import os
import csv

# Path to collect data from the Resources folder
dataCSV = os.path.join('Resources', 'election_data.csv')

# Clear the screen for enhanced user visiblity
os.system('cls' if os.name == 'nt' else 'clear')

print()
print('Election Results')
print()
print('--------------------------')
print()

# Open the CSV file --> Calculate total votes based on the number of rows in dataset, less the header row

with open(dataCSV, 'r', newline = '') as datafile:
    totalrows = len(datafile.readlines())
    totalvotes = totalrows - 1
    print("Total Votes: ",totalvotes)
    print()
    print('--------------------------')
    print()

# Open the CSV file --> read the data into a list: candidate_list
with open(dataCSV, newline='') as datafile:
    headerline = next(datafile)
    candidate_list = []
    for row in csv.reader(datafile, delimiter = ','):
        candidate_item = row[2]
        candidate_list.append(candidate_item)

# Identify the unique candidate names --> use the candidate_list above to create a set of unique candidate names, then count the number of candidates
candidate_unique = set(candidate_list)
number_candidates = len(candidate_unique)
candidate_unique_list = list(candidate_unique)


# Count the number of votes each candidate received --> number of times each candidate's name appears in the candidate_list

# Loop through the votes one time for each of the candidates and count the number of votes each candidate receives
for i in range(number_candidates):
    print()
    print(list(candidate_unique)[i],":",round(candidate_list.count(list(candidate_unique)[i]) / totalvotes * 100, 3),"%","(",candidate_list.count(list(candidate_unique)[i]),")")
 
print()
print('--------------------------')
print()

# Determine the winner
# Loop through the vote results and, for each unique candidate, store their total votes received as an element in a list, vote_count_list (will have 4 values)
# Then find the index position in the list for the max votes received
# Then apply this index to the set of candidate_unique_list to determine the name of the winner (Had to convert candidate_unique set to a list in order to index)

vote_count_list = []
for i in range(number_candidates):
    vote_count_item = candidate_list.count(list(candidate_unique)[i])
    vote_count_list.append(vote_count_item)
winner_vote_count = max(vote_count_list)
index_vote_count = vote_count_list.index(winner_vote_count)
print("Winner:",candidate_unique_list[index_vote_count])
print()
print('--------------------------')

