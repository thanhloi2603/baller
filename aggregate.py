from sheet_converter import convert_xlsx_to_csv, TransactionManager
from user import Usermanager


def main():
    um = Usermanager()
    um.import_from_file('users.csv')

    for user in um.get_remission_users():
        print(user)


if __name__ == '__main__':
    convert_xlsx_to_csv('input_sheets/SaoKeTK_01032025_11032025.xlsx')
    main()

tm_manager = TransactionManager()
tm_manager.import_from_techcombank_csv_file("input_sheets/SaoKeTK_01032025_11032025.csv")

for transaction in tm_manager.transactions:
    print(transaction.date, transaction.description, transaction.amount, transaction.direction)
