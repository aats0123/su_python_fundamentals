class BankAccount:
    def __init__(self, name, bank, balance):
        self.name = name
        self.bank = bank
        self.balance = balance


accounts = []
_input = input()
while not _input == 'end':
    _input = list(_input.split(' | '))
    bank = _input[0]
    name = _input[1]
    balance = float(_input[2])
    account = BankAccount(name, bank, balance)
    accounts.append(account)
    _input = input()
sorted_accounts = sorted(accounts, key=lambda a: (-a.balance, len(a.bank)))

for account in sorted_accounts:
    print(f'{account.name} -> {account.balance:.2f} ({account.bank})')
