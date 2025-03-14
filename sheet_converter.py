import openpyxl
import csv
import os
from dateutil.parser import parse


def convert_xlsx_to_csv(input_file_path, output_file_path):
    # Load the XLSX file
    wb = openpyxl.load_workbook(input_file_path)

    sheet = wb.active

    # Create a CSV file
    with open(output_file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for row in sheet.rows:
            writer.writerow([cell.value for cell in row])


def string_to_integer(s):
  """Converts a string with commas to an integer."""
  try:
    # Remove commas and convert to integer
    return int(s.replace(",", ""))
  except ValueError:
    return 0  # Handle cases where the string is not a valid number


class Transaction:
    def __init__(self, date, description, amount, direction):
        self.date = date
        self.description = description
        self.amount = string_to_integer(amount)
        self.direction = direction
        self.owner = None
    
    def set_owner(self, user):
        self.owner = user

    def __str__(self):
        return f"{self.date}, {self.description}, {self.amount}, {self.direction}"


class TransactionManager:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction: Transaction):
        self.transactions.append(transaction)

    def get_all_transactions(self):
        for transaction in self.transactions:
            yield transaction
    
    def get_income_transactions(self):
        for transaction in self.transactions:
            if transaction.direction == "income":
                yield transaction

    def get_outcome_transactions(self):
        for transaction in self.transactions:
            if transaction.direction == "outcome":
                yield transaction

    @property
    def accumlated_outcome_amount(self):
        return sum([transaction.amount for transaction in self.get_outcome_transactions()])

    def get_income_transactions_without_owner(self):
        for transaction in self.transactions:
            if transaction.direction == "income" and transaction.owner is None:
                yield transaction

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
