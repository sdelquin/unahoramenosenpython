data = {
    'user': True,
    'name': 'Peter Parker'
}


# match data:
#     case {'user': int(age)}:
#         print(data['name'], age)

# items = [1, 2, 3, 4]
# match items:
#     case (first, *rest, last):
#         print(first, rest, last, sep='|')


data = [
    {
        'user': 7,
        'name': 'Peter Parker',
        'hero': 'Spiderman',
    }, {
        'user': 'ab5b9abf-b417-44a5-acfe-690e61b49e12',
        'name': 'Adrian',
        'alterego': 'Ozymandias',
    },
    {
        'user': 12.23,
        'name': 'Bruce Wayne',
        'alterego': 'Batman',
    },
]

# for user in data:
#     match user:
#         case {'user': int()}:
#             print(user['name'], user['hero'])
#         case {'user': str()}:
#             print(user['name'], user['alterego'])

for user in data:
    match user:
        case {'user': int()} if len(user['name']) > 7:  # guards
            print(user['name'], user['hero'])
        case {'user': str()}:
            print(user['name'], user['alterego'])
        case _:
            print('cool')
