#!/usr/bin/env python
users = [
    { 'admin': True, 'active': True, 'name': 'sasha' },
    { 'admin': True, 'active': False, 'name': 'coco' },
    { 'admin': False, 'active': False, 'name': 'popi' },
    { 'admin': True, 'active': False, 'name': 'rio' },
]

line = 1
for user in users:
    if user['admin'] and user['active']:
       print("%s ACTIVE - (ADMIN) %s" % (line, user['name']))
    elif user['admin']:
       print("%s (ADMIN) %s" % (line, user['name']))
    elif user['active']:
       print("%s ACTIVE - %s" % (line, user['name']))
    else:
       print("%s %s" % (line, user['name']))
    line += 1
