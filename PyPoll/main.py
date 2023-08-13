#Import Libraries
import os
import csv

#Create the file path
file = os.path.join("Resources", "election_data.csv")

#Open the CSV to see what we're working with
with open(file, newline = "") as filePath:
    csvreader = csv.reader(filePath, delimiter=",")
    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    #Total Number of votes
    #List of Candidates that received votes
    #make a list to capture the amount of votes so we can run a len() function
    #same as above, but we need a function to extract unique names, found out set() accomplishes this
    vote = []
    uniqueCandidate = []
    diana = []
    charles = []
    raymon = []

    for row in csvreader:
       vote.append(row[0])
       uniqueCandidate.append(row[2])
       if row[2] == "Diana DeGette":
        diana.append(row[0])
       elif row[2] == "Charles Casper Stockham":
        charles.append(row[0])
       elif row[2] == "Raymon Anthony Doane":
        raymon.append(row[0])

    votettl = len(vote)
    uqeCand = set(uniqueCandidate)
    
    #Total number of votes each candidate got
    diana = len(diana)
    charles = len(charles)
    raymon = len(raymon)

    #% of votes each candidate won
    #Pretty simple and we've done this in the pyBank excercise.
    #Take the variable we created for total each candidates' total votes and divide them by the
    #total number of votes, and then multiply that by 100. Then to get 3 decimal points, use format().
    pctDiana = (diana/votettl) * 100
    pctDiana = format(pctDiana,".3f")

    pctCharles = (charles/votettl) * 100
    pctCharles = format(pctCharles, ".3f")

    pctRaymon = (raymon/votettl) * 100
    pctRaymon = format(pctRaymon, ".3f")

    #The Winner of the election
    #In this case, we can take the variable for the total votes for each winner and just run a max()
    winner = [diana,charles,raymon]
    if max(winner) == diana:
        won = 'Diana DeGette'
    elif max(winner) == charles:
        won = 'Charles Casper Stockham'
    elif max(winner) == raymon:
        won = 'Raymon Anthony Doane'



    print("Election Results")
    print("------------------------------------")
    print("Total Votes: " + str(votettl))
    print("------------------------------------")
    print(f"Charles Casper Stockham:  {pctCharles}%  ({charles})")
    print(f"Diana DeGette : {pctDiana}%  ({diana})")
    print(f"Raymon Anthony Doane:  {pctRaymon}%  ({raymon})")
    print("------------------------------------")
    print(f"Winner: {won}")
    print("------------------------------------")

# Now we'll write export our analysis as a txt file
outPath = os.path.join("Analysis", "Election_Analysis_Output.txt")         
elecRes = open(outPath, "w")
elecRes.write("Election Results" + "\n")
elecRes.write("-----------------------------------------" + "\n")
elecRes.write(f"Total Votes: {votettl}" + "\n")
elecRes.write("-----------------------------------------" + "\n")
elecRes.write(f"Charles Casper Stockham:  {pctCharles}%  ({charles})" + "\n")
elecRes.write(f"Diana DeGette : {pctDiana}%  ({diana})" + "\n")
elecRes.write(f"Raymon Anthony Doane:  {pctRaymon}%  ({raymon})" + "\n")
elecRes.write("------------------------------------------" + "\n")
elecRes.write(f"Winner: {won}" + "\n")
elecRes.write("------------------------------------------")