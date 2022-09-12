#!/usr/bin/python3

if __name__ == "__main__":

    from sys import argv
    import requests
    import json

    id = argv[1]

    urlUser = 'https://jsonplaceholder.typicode.com/users/' + argv[1]
    response_name = requests.get(urlUser)
    name = response_name.json()['username']

    urlTodo = urlUser + '/todos'
    response_todos = requests.get(urlTodo)
    task = response_todos.json()

    my_list = []
    for element in task:
        my_dict = {
            'task': element['title'],
            'completed': element['completed'],
            'username': name
            }
        my_list.append(my_dict)

    json_dump = json.dumps({argv[1]: my_list})

    with open(argv[1] + '.json', "w") as outfile:
        outfile.write(json_dump)
