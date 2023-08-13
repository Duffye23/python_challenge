#Import Libraries
import os
import csv

#create a variable for the file path
file = os.path.join("Resources","budget_data.csv")

#Open the CSV to see what we're working with
with open(file, newline = "") as filePath:
    csvreader = csv.reader(filePath, delimiter=",")
    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    #The total number of months included in the dataset
    #The net total amount of "Profit/Losses" over the entire period
    #make a list to capture the amount of months so we can run a len() function
    #same as above with months, we're going to add each input in the Profit/Losses column into a list and then sum it
    nbrMonths = []
    pl = []

    #run through the dataset and add each row's month to the list
    for row in csvreader:
       nbrMonths.append(row[0])
       pl.append(row[1])

    #Take the list we have of the months and use len() to find the total months
    months = len(nbrMonths)
      
    #We need to turn the list into integers in order to perform arithmetic manipulations
    for i in range(0, len(pl)):
        pl[i] = int(pl[i])
    
    sumpl = sum(pl)
    
    #The changes in "Profit/Losses" over the entire period, and then the average of those changes
    #So I think the want a month over list of changes within the dataset, and then to average these out
    #In which case we need a list that houses these changes.
    revChg = []
    for rev in range(1, len(pl)):
        revChg.append((int(pl[rev]) - int(pl[rev-1])))
    
    #We can now average this new list out
    avgChg = sum(revChg)/len(revChg)
    #we get a number with more than 2 decimal poitns, which we don't want so we'll convert it to 2
    avgChg = format(avgChg,".2f")
    
    
    #The greatest increase in profits (date and amount) over the entire period
    #So we can probably just run a max function right?
    maxChg = max(revChg)
    #we can use index() and max() to search through the column, which is why the +1 is there
    #to shift it from index 0 to 1
    maxmonth = str(nbrMonths[revChg.index(max(revChg))+1])
    
    #The greatest decrease in profits (date and amount) over the entire period
    #Same with the Min and the month
    minChg = min(revChg)
    minmonth = str(nbrMonths[revChg.index(min(revChg))+1])
    
    #Now to make it look like how the assignemnt wants:
    print("")
    print("Financial Analysis")
    print("------------------------------------")
    print(f"Total Number of months in the in the dataset: {months}")
    print(f"The net total amount of Profit/Losses is : ${sumpl}")
    print(f"The Average change of month to month 'Profit/Losses: ${avgChg}")
    print(f"The greatest INCREASE in the 'Profit/Losses' column is: {maxmonth}: ${maxChg}")
    print(f"The greatest DECREASE in the 'Profit/Losses' column is: {minmonth}: ${minChg}")

# Now we'll write export our analysis as a txt file
outPath = os.path.join("Analysis", "Financial_Analysis_Output.txt")         
finAna = open(outPath, "w")
finAna.write("Financial Analysis" + "\n")
finAna.write("-----------------------------------------" + "\n")
finAna.write(f"Total Number of months in the dataset: {months}" + "\n")
finAna.write(f"The net total amount of Profit/Losses is : ${sumpl}" + "\n")
finAna.write(f"The Average change of month to month 'Profit/Losses: ${avgChg}" + "\n")
finAna.write(f"The greatest INCREASE in the 'Profit/Losses' column is: {maxmonth}: (${maxChg})" + "\n")
finAna.write(f"The greatest DECREASE in the 'Profit/Losses' column is: {minmonth}: (${minChg})" + "\n")
finAna.close()
