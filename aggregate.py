import os
from sheet_converter import convert_xlsx_to_csv, TransactionManager
from user import Usermanager


def setup():
    input_file_path = 'input_sheets/SaoKeTK_01032025_11032025.xlsx'
    csv_file_path = os.path.join(os.path.dirname(input_file_path), os.path.splitext(os.path.basename(input_file_path))[0] + '.csv')
    convert_xlsx_to_csv(input_file_path, csv_file_path)
    um = Usermanager()
    um.import_from_file('users.csv')

    tm_manager = TransactionManager()
    tm_manager.import_from_techcombank_csv_file(csv_file_path)


if __name__ == '__main__':
    setup()
