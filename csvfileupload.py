import csv


def calculate_salary(hours_worked, hourly_rate):
    if hours_worked < 0 or hourly_rate < 0:
        print("Invalid inputs")

    regular_hours = min(hours_worked, 40)  # Max 40 hours regular
    overtime_hours = max(0, hours_worked - 40)  # Overtime if more than 40 hours
    overtime_rate = hourly_rate * 1.5  # Overtime pay is 1.5x

    salary = (regular_hours * hourly_rate) + (overtime_hours * overtime_rate)
    return round(salary, 2)  # Round salary to 2 decimal places


with open('input.csv', mode='r', newline='') as infile:  # Reads the starter input excel sheet file
    reader = csv.reader(infile)
    header = next(reader)

    processed_data = [header + ["WeeklySalary"]]  # Add new column for salary
    dependents = [header + ["Dependents"]]

    for row in reader:
        employee_id, name, hours, rate = row
        weekly_salary = calculate_salary(float(hours), float(rate))
        processed_data.append([employee_id, name, hours, rate, weekly_salary])

with open('output.csv', mode='w', newline='') as outfile:  # This writes to the output csv file

    writer = csv.writer(outfile)
    writer.writerows(processed_data)

print("Check output.csv")
