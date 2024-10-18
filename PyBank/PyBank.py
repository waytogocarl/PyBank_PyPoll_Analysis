import csv
import os

# files to load etc.
budget_data_csv = os.path.join(".", "budget_data.csv")
budget_analysis = os.path.join(".", "budget_analysis.txt")

#creating dictionaries for the biggest increase and biggest decrease with keys and values
biggest_increase = {"month": "", "change": 0}
biggest_decrease = {"month": "", "change": float("inf")}

# define the variables
total_months = 0
net_total = 0
months = []
monthly_changes = []

# open and read the CSV file
with open(budget_data_csv) as budgetdata:
    reader = csv.reader(budgetdata)
    header = next(reader)

# extract the header row, so that it doesn't affect the calculations
    first_row = next(reader)

# create the calculation for tracking the total & net changes
    total_months = total_months + 1
    net_total = net_total + int(first_row[1])
    prev_value = int(first_row[1])

# loop through the rows and use the calculations from above ^
    for row in reader:

        # track the totals
        total_months = total_months + 1
        current_value = int(row[1])
        net_total += current_value

        # track the net change
        monthly_change = current_value - prev_value
        prev_value = current_value

        months.append(row[0])
        monthly_changes.append(monthly_change)

        #calculate the biggest increase
        if monthly_change > biggest_increase["change"]:
            biggest_increase["month"] = row[0]
            biggest_increase["change"] = monthly_change
        
        #calculate the biggest decrease
        if monthly_change < biggest_decrease["change"]:
            biggest_decrease["month"] = row[0]
            biggest_decrease["change"] = monthly_change

#calculate the average change across all the months
average_change = sum(monthly_changes) / len(monthly_changes)

output = (
# print the data
    f"Budget Analysis\n"
    f"--------------------------------\n"
    f"Total Months: {total_months}\n"
    f"Net Total: ${net_total}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Biggest Increase in Profits: {biggest_increase['month']} (${biggest_increase['change']})\n"
    f"Biggest Decrease in Profits: {biggest_decrease['month']} (${biggest_decrease['change']})\n"
)

print(output)

with open(budget_analysis, "w") as txt_file:
    txt_file.write(output)


