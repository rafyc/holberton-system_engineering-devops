#!/usr/bin/python3
'''
Python script to export data in the JSON format.
'''
if __name__ == "__main__":

    import json
    import requests
    from sys import argv

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
