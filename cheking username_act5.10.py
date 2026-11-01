current_users = ['Admin', 'tazkia', 'thaya', 'ais', 'fathma']
new_users = ['thaya', 'Eko', 'tazkia', 'Fajar', 'Gita']

current_users_lower = []
for user in current_users:
    current_users_lower.append(user.lower())

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"{new_user}: already used. Please enter a new username.")
    else:
        print(f"{new_user}: username is available.")