import openpyxl
import csv
import os
from dateutil.parser import parse



def convert_xlsx_to_csv(input_file_path):
    # Load the XLSX file
    wb = openpyxl.load_workbook(input_file_path)
    csv_file_path = os.path.join(os.path.dirname(input_file_path), os.path.splitext(os.path.basename(input_file_path))[0] + '.csv')

    sheet = wb.active

    # Create a CSV file
    with open(csv_file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for row in sheet.rows:
            writer.writerow([cell.value for cell in row])


def read_csv_file(csv_file_path):
    with open(csv_file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            try:
                parse(row[1])  # Try to parse the 2nd column as a date
                print(row)  # If successful, print the entire row
            except ValueError:
                pass  # If not successful, skip to the next row


convert_xlsx_to_csv('input_sheets/SaoKeTK_01032025_11032025.xlsx')
read_csv_file("input_sheets/SaoKeTK_01032025_11032025.csv")
