import csv

class User:
    def __init__(self, id: str, name: str, remission: bool, cues: list = []):
        self.id = id
        self.name = name.strip()
        self.remission = remission
        self.cues = cues
        self.transactions = []
    
    def own_transaction(self, transaction):
        self.transactions.append(transaction)
        transaction.set_owner(self)

    def __str__(self):
        return f'{self.id} - {self.name}, Remission: {self.remission}, Cues: {", ".join(self.cues)}'


class Usermanager:
    def __init__(self):
        self.users = []
    
    def add_user(self, user: User):
        self.users.append(user)

    def get_all_users(self):
        for user in self.users:
            yield user
    
    def get_remission_users(self):
        return [user for user in self.users if user.remission]

    def search_transaction_owner(self, transaction_description: str):
        for user in self.get_all_users():
            for cu in user.cues:
                if cu and cu.strip().lower() in transaction_description.lower():
                    return user

    def import_from_file(self, csv_file_path):
        with open(csv_file_path, mode='r', encoding='utf-8') as file:
            csv_reader = csv.reader(file, delimiter=',')
            for row in csv_reader:
                id = row[0]
                if not str(id).isnumeric():
                    continue
                name = row[1]
                cues = row[3].split(', ')
                remission = row[2].strip() == 'y'
                self.add_user(User(id, name, remission, cues)) 
