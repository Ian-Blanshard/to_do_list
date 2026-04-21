from lib.todo import *

"""
When a todo instance is completed complete is set to False
and task is set to the correct string
"""
def test_todo_init():
    todo_one = Todo('Washing up')
    assert todo_one.task == 'Washing up'
    assert todo_one.complete == False