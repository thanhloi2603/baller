import csv

class User:
    def __init__(self, id: str, name: str, remission: bool):
        self.id = id
        self.name = name.strip()
        self.remission = remission

    def __str__(self):
        return f'{self.id} - {self.name}'


class Usermanager:
    def __init__(self):
        self.users = []
    
    def add_user(self, user: User):
        self.users.append(user)

    def get_all_users(self):
        return self.users
    
    def get_remission_users(self):
        return [user for user in self.users if user.remission]


um = Usermanager()

with open('users.csv', mode='r', encoding='utf-8') as file:
    csv_reader = csv.reader(file, delimiter=',')
    for row in csv_reader:
        um.add_user(User(row[0], row[1], row[2].strip() == 'y'))

for user in um.get_remission_users():
    print(user)
