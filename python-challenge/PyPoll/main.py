# import modules 
import os
import csv

# set path for csv file to load from Resources  
Poll_csv = os.path.join("Resources","election_data.csv")
# set path for text file to output to Analysis 
Poll_text = os.path.join("Analysis", "Pypoll_analysis.txt")

# creating a list counting every count of all candidates 
all_candidates = []

# assigning variables for count 
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0

# read Poll_csv that is election_data.csv & skip the header with next 
with open(Poll_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvfile)

    for row in csvreader:
        
        # calculating total number of votes put into list all_candidates 
        all_candidates.append(row[2])
        
        # calculating votes each individual candidate won 
        if (row[2] == "Khan"):
            khan_votes += 1
        elif (row[2] == "Correy"):
            correy_votes += 1
        elif (row[2] == "Li"):
            li_votes += 1
        else:
            otooley_votes += 1
            
    # calculating percentages 
    kahn_percent = khan_votes / len(all_candidates)
    correy_percent = correy_votes / len(all_candidates)
    li_percent = li_votes / len(all_candidates)
    otooley_percent = otooley_votes / len(all_candidates)
    
    # calculating winner 
    winner = max(khan_votes, correy_votes, li_votes, otooley_votes)

    if winner == khan_votes:
        winner_name = "Khan"
    elif winner == correy_votes:
        winner_name = "Correy"
    elif winner == li_votes:
        winner_name = "Li"
    else:
        winner_name = "O'Tooley" 

output =(
f"Election Results\n"
f"------------------------\n"
f"Total Votes: {len(all_candidates)}\n"
f"---------------------------\n"
f"Kahn: {kahn_percent:.3%}({khan_votes})\n"
f"Correy: {correy_percent:.3%}({correy_votes})\n"
f"Li: {li_percent:.3%}({li_votes})\n"
f"O'Tooley: {otooley_percent:.3%}({otooley_votes})\n"
f"-------------------------\n"
f"Winner: {winner_name}\n"
f"-------------------------\n"
)
print(output)

# writting on text file 
with open(Poll_text, "w") as text:
    text.write(output)