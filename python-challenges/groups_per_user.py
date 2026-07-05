#!/usr/bin/python3
# written by: atholcomb
# groups_per_user.py

def groups_per_user(group_dictionary):
    user_groups = {}
    for groups, users in group_dictionary.items():
        for user in users:
            user_groups.setdefault(user, []).append(groups)
    
    return user_groups


print(groups_per_user({"local": ["admin", "userA"],"public":["admin", "userB"], "administrator": ["admin"] }))
