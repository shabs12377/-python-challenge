import os
import csv
csvpath = os.path.join("Resources", "election_data.csv")
#the total number of votes cast
total_votes = 1
#list of candidates who recieved votes
candidates_dictionary = {}
#percentage of candidates won
winning_candidates = ()
#total number of votes candidates won
number_of_winning_votes = ()
#winner of election based on popular votes
popular_vote = ()


with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    # skip the first row for total number of votes cast
    # add first row's vote to net vote
 
    

    
    for row in csvreader:
        total_votes = total_votes + 1
        candidate=row[2]
        county=row[1]
        if candidate in candidates_dictionary:
            candidates_dictionary[candidate]+=1
        else:  
            candidates_dictionary[candidate]=1

winner_votes=0
winner_name=""


for key in candidates_dictionary.keys():
    candidate=key
    votes=candidates_dictionary[key]
    print (f"{candidate} has {votes} votes") 
    if votes>winner_votes:
        winner_name=candidate
        winner_votes=votes
print(winner_votes,winner_name)
percentage = (winner_votes / total_votes) * 100 
print(f"percentage of {winner_votes}") 