import os
from sheet_converter import convert_xlsx_to_csv, TransactionManager
from user import Usermanager


def setup():
    input_file_path = 'input_sheets/SaoKeTK_01012025_12032025.xlsx'
    csv_file_path = os.path.join(os.path.dirname(input_file_path), os.path.splitext(os.path.basename(input_file_path))[0] + '.csv')
    convert_xlsx_to_csv(input_file_path, csv_file_path)
    um = Usermanager()
    um.import_from_file('users.csv')

    tm_manager = TransactionManager()
    tm_manager.import_from_techcombank_csv_file(csv_file_path)
    return um, tm_manager


if __name__ == '__main__':
    um, tm_manager = setup()
    for transaction in tm_manager.get_income_transactions():
        if user := um.search_transaction_owner(transaction.description):
            user.own_transaction(transaction)
            # print(f'{user.name} - {transaction.description} - {transaction.amount}')

    print("======== Transactions without owner ========")
    for transaction in tm_manager.get_income_transactions_without_owner():
        print(transaction)

    print("======== Print users ========")
    for user in um.get_all_users():
        print(f"{user.name} - {user.amount}")
        monthly_amounts = user.get_amount_by_month()
        if monthly_amounts:
            print(f"  Monthly amounts:")
            for month, amount in monthly_amounts.items():
                print(f"    {month}: {amount}")
