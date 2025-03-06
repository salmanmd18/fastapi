from fastapi import FastAPI

api = FastAPI()

all_todos = [
    {'todo_id': 1, 'todo_name': 'sports', 'todo_description': 'Go to the gym'},
    {'todo_id': 2, 'todo_name': 'read', 'todo_description': 'read 10 pages'},
    {'todo_id': 3, 'todo_name': 'shop', 'todo_description': 'Go shopping'},
    {'todo_id': 4, 'todo_name': 'study', 'todo_description': 'study for exams'},
    {'todo_id': 5, 'todo_name': 'meditate', 'todo_description': 'meditate 20 min'}
    ]

@api.get('/')
def index():
    return {"message": "hello" }

@api.get('/calculation')
def caluculation():
    pass
    return 

@api.get('/getdata')
async def get_data_from_db():
    await request
    pass
    return

@api.get('/todos/{todo_id}')
def get_todo(todo_id: int):
    for todo in all_todos:
        if todo['todo_id'] == todo_id:
            return {'result': todo}

@api.get('/todos')
def get_todos(first_n :int = None):
    if first_n:
        return all_todos[: first_n]
    else:
        return all_todos
