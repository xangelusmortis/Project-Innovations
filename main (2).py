
import csv

employeeID = 0
firstName = "John"
lastName = "Doe"
numberDependents = 0
hoursWorked = 5
hourlyRate = 12

regular_hours = 0
over_hours = 0
overtimeRate = 0

stateTax = 0.056
fedTax = 0.079

totalTax = stateTax + fedTax
gross = hoursWorked * hourlyRate
postTax = gross - totalTax


def gross_calculation(hours_worked, hourly_pay):  # Before tax and deductions
    if hours_worked < 0 or hourly_pay < 0:
        print("Invalid entry")
    regular_hours = min(hoursWorked, 40)
    overtimeHours = max(0, hoursWorked - 40)
    overtimeRate = hourlyRate * 1.5
    gross = (regular_hours * hourlyRate) + (overtimeHours * overtimeRate)
    return round(gross, 2)


def deductions():
    stateTax = gross * 0.056
    fedTax = gross * 0.079
    return stateTax, fedTax


print("Gross pay:", gross_calculation(hoursWorked,hourlyRate))
deductions()
