import requests
import sys

auth_params={
    'key':"5340b523b5383cbc5024eda3de9d0cfa",
    'token':"2a7c509349e1c3256a2bc3e2b80730678c6f28ba4a7737a1ced4886ee220089f"
}

base_url = "https://api.trello.com/1/{}"
board_id="73BRduQc"

def read():
    column_data=requests.get(base_url.format('boards')+'/'+board_id+'/lists',params=auth_params).json()

    for column in column_data:
        print(column['name'])
        task_data = requests.get(base_url.format('lists') + '/' + column['id'] + '/cards', params=auth_params).json()
        if not task_data:
            print('\t' + 'Нет задач!')
            continue
        for task in task_data:
            print('\t' + task['name'])


def create(name, column_name):
    # Получим данные всех колонок на доске
    column_data = requests.get(base_url.format('boards') + '/' + board_id + '/lists', params=auth_params).json()

    # Переберём данные обо всех колонках, пока не найдём ту колонку, которая нам нужна
    for column in column_data:
        if column['name'] == column_name:
            # Создадим задачу с именем _name_ в найденной колонке
            requests.post(base_url.format('cards'), data={'name': name, 'idList': column['id'], **auth_params})
            break

if __name__ == "__main__":
    if len(sys.argv) <= 2:
        read()
    else:
	    create(sys.argv[2], sys.argv[3])