#PyPoll
import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')
#The dataset is composed of 3 columns: `Voter ID', 'Country' and `Candidate`
#print(csvpath)
with open(csvpath, newline='') as csvfile:

#     # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

#   Skip the header row 
    csv_header = next(csvreader, None)

    total_votes = 0
    candidates = []
    candidate_vote = {}

# The total number of votes cast
    for row in csvreader:
        total_votes = total_votes + 1

# A complete list of candidates who received votes
        candidate_names = row[2]
        if row[2] not in candidates:
            candidates.append(candidate_names)
            candidate_vote[row[2]]=1
        else:
            candidate_vote[row[2]]+=1

    # print(candidate_vote)
    # print(candidates)

    # The percentage of votes each candidate won str(total candidates votes/total votes * 100),
    # The total number of votes each candidate won
    # The winner of the election based on popular vote.

    # print(total_votes)
    # print(candidate_vote[candidate])
    # print(candidate_vote[candidate]/total_votes)
    # print(percent_wins)

    # print(winner)

# As an example, your analysis should look similar to the one below:
# Election Results
# -------------------------
# Total Votes: 3521001
# -------------------------
# Khan: 63.000% (2218231)
# Correy: 20.000% (704200)
# Li: 14.000% (492940)
# O'Tooley: 3.000% (105630)
# -------------------------
# Winner: Khan
# -------------------------

print(" ")
print("Election Results")
print("----------------------------")
print(f"Total Votes: {total_votes}")
print("----------------------------")
for candidate in candidate_vote:
    percent_wins = round((candidate_vote[candidate]/total_votes) * 100)
    candidate_votes =(f"{candidate}: {percent_wins}% ({candidate_vote[candidate]})")
    print(candidate_votes)
    winner = max(candidate_vote, key=candidate_vote.get)

print("----------------------------")
print(f"Winner: {winner}")
print("----------------------------")
# In addition, your final script should both print the analysis to the terminal and export a text file with the results.

# Open the file using "write" mode. Specify the variable to hold the contents
with open("PyPoll_output.txt", "w") as txtfile:
    txtfile.write(" \n")
    txtfile.write("Election Results \n")
    txtfile.write("---------------------------- \n")
    txtfile.write(f"Total Votes: {total_votes} \n")
    txtfile.write("---------------------------- \n")
    txtfile.write(f"{candidate_votes} \n")
    txtfile.write("---------------------------- \n")
    txtfile.write(f"Winner: {winner}")
    txtfile.write("---------------------------- \n")
    txtfile.close()
