#!/usr/bin/python3
'''
Python script to export data in the JSON format.
'''

if __name__ == "__main__":

    import json
    import requests
    from sys import argv


    urlUser = 'https://jsonplaceholder.typicode.com/users/'
    all_user = requests.get(urlUser).json()
    dico = {}

    for users in all_user:
        id = users['id']
        name = users['username']
        urlTodo = urlUser + str(id) + '/todos'

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
        dico[id] = my_list

    json_dump = json.dumps(dico, indent=4)

    with open('todo_all_employees.json', "w") as outfile:
        outfile.write(json_dump)
