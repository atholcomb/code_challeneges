#!/usr/bin/python3
# written by: atholcomb
# email_list.py
# For each user in list, print out user with respective domain attached
# ['clark.kent@gmail.com', 'diana.prince@gmail.com', 'peter.parker@gmail.com', 'barbara.gordon@yahoo.com', 'jean.grey@yahoo.com', 'bruce.wayne@hotmail.com']

def email_list(domains):
    emails = []
    for domains, users in domains.items():
        for user in users:
            emails.append(user+'@'+domains)
    return emails
    

print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))
