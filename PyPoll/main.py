import os
import csv
csvpath = os.path.join("Resources", "election_data.csv")
#the total number of votes cast
total_votes = 1
#list of candidates who recieved votes
candidates_list = []
#percentage of candidates won
candidate_dict={}
winning_candidates = []
#total number of votes candidates won
number_of_winning_votes = ()
#winner of election based on popular votes
popular_vote = ()
winning_count=0
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    # skip the first row for total number of votes cast
    # add first row's vote to net vote
 
    for row in csvreader:
        total_votes = total_votes + 1
        candidate=row[2]
        county=row[1]
        if candidate not in candidates_list:
            candidates_list.append(candidate)
            candidate_dict[candidate]=0
        candidate_dict[candidate]=candidate_dict[candidate]+1
    print("Total Votes"+"\n"+str(total_votes))
winner_votes=0
winner_name=""
for key in candidate_dict:
    candidate=key
    votes=candidate_dict.get(candidate)
    votes_percent=float(votes)/float(total_votes)*100
    # print (f"{candidate} has {votes} votes") 
    if votes>winning_count:
        winner_name=candidate
        winning_count=votes
    print(f"{candidate}:{votes_percent:.3f}")