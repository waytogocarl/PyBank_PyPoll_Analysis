#import CSV file
import csv
import os

#files to load and files to output
election_data_csv = os.path.join(".", "election_data.csv")
poll_analysis = os.path.join(".", "poll_analysis.txt")

#define variables
total_votes = 0
candidate_votes = {}
winning_candidate = ""
winning_count = 0

#open and read the CSV file, skip the header row
with open(election_data_csv) as election_data:
    reader = csv.reader(election_data)
    header = next(reader)

    #loop through the rows
    for row in reader:
        total_votes += 1
        candidate_name = row[2]

        if candidate_name not in candidate_votes:
            candidate_votes[candidate_name] = 0

        candidate_votes[candidate_name] += 1

#open the output file and tell it what to print
with open(poll_analysis, "w") as txt_file:
    election_results = (
        f"Election Results\n"
        f"--------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"---------------------------\n"
    )

    #print the total vote count
    print(election_results)
    txt_file.write(election_results)

    #loop through the candidates to find out the winner
    for candidate, votes in candidate_votes.items():
        vote_percentage = (votes / total_votes) * 100

        if votes > winning_count:
            winning_count = votes
            winning_candidate = candidate

        #print the vote counts and percentages
        candidate_results = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(candidate_results, end="")
        txt_file.write(candidate_results)

    #generate the winning summary table
    winning_summary = (
        f"---------------------\n"
        f"Winner: {winning_candidate}\n"
        f"---------------------\n"
    )

    #print the winning candidate to the summary table
    print(winning_summary)
    txt_file.write(winning_summary)



    