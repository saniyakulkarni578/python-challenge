# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("PyBank","Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("PyBank","analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
net_change_list = []
months = []

# Open and read the csv file properly
with open(file_to_load, mode='r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    
    # Skip the header row
    csv_header = next(csv_reader)

    # Extract the first row to set initial values for calculations
    first_row = next(csv_reader)
    total_months += 1
    total_net += int(first_row[1])
    previous_net = int(first_row[1])

    # Process each row of data
    for row in csv_reader:
        # Track the total number of months
        total_months += 1
        
        # Track the total net amount of "Profit/Losses"
        total_net += int(row[1])

        # Calculate the monthly net change and add to list
        net_change = int(row[1]) - previous_net
        previous_net = int(row[1])
        net_change_list.append(net_change)
        months.append(row[0])

    # Calculate the greatest increase in profits (date and amount)
    greatest_increase = max(net_change_list)
    greatest_increase_month = months[net_change_list.index(greatest_increase)]

    # Calculate the greatest decrease in losses (date and amount)
    greatest_decrease = min(net_change_list)
    greatest_decrease_month = months[net_change_list.index(greatest_decrease)]

    # Calculate the average net change across the entire period
    average_change = sum(net_change_list) / len(net_change_list)

# Generate the output summary with the exact formatting needed
output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n"
    f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n"
)

# Print the output to the terminal
print(output)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
