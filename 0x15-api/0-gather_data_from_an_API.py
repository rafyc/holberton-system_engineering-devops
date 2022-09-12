#!/usr/bin/python3
'''Python script that, using this REST API, for a given employee ID,
returns information about his todo list progress.
'''
if __name__ == "__main__":

    from sys import argv
    import requests

    urlUser = 'https://jsonplaceholder.typicode.com/users/' + argv[1]
    response_name = requests.get(urlUser)
    name = response_name.json()['name']

    urlTodo = urlUser + '/todos'
    response_todos = requests.get(urlTodo)
    task = response_todos.json()
    total_task = len(task)

    count = 0
    for element in task:
        if element['completed'] is True:
            count += 1

    print("Employee {} is done with tasks({}/{}):".format(name, count,
          total_task))

    for element in task:
        if element['completed'] is True:
            task_name = element['title']
            print("\t{}".format(task_name))
