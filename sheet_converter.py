import openpyxl
import csv
import os


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


convert_xlsx_to_csv('input_sheets/SaoKeTK_01032025_11032025.xlsx')
