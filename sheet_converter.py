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


class Transaction:
    def __init__(self, date, description, amount, direction):
        self.date = date
        self.description = description
        self.amount = amount
        self.direction = direction


class TransactionManager:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction: Transaction):
        self.transactions.append(transaction)

    def import_from_techcombank_csv_file(self, csv_file_path):
        with open(csv_file_path, 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                try:
                    parse(row[1])  # Try to parse the 2nd column as a date
                    _date = row[1]
                    _description = row[17]
                    if row[31]:
                        _amount = row[31]
                        _direction = "outcome"
                    else:
                        _amount = row[37]
                        _direction = "income"
                    self.add_transaction(Transaction(_date, _description, _amount, _direction))
                except ValueError:
                    pass  # If not successful, skip to the next row
