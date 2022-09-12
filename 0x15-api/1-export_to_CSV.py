#!/usr/bin/python3
'''
Python script to export data in the CSV format.
'''
if __name__ == "__main__":

    import csv
    import requests
    from sys import argv

    urlUser = 'https://jsonplaceholder.typicode.com/users/' + argv[1]
    response_name = requests.get(urlUser)
    name = response_name.json()['username']

    urlTodo = urlUser + '/todos'
    response_todos = requests.get(urlTodo)
    task = response_todos.json()
    total_task = len(task)

    with open('{}.csv'.format(argv[1]), 'w', encoding='UTF8') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for element in task:
            writer.writerow([argv[1], name, element['completed'],
                            element['title']])
