from lib.todo_list import *

"""
When a TodoList instance is created incomplete returns an empty list
"""
def test_incompleted_empty_list():
    my_todo_list = TodoList()
    assert my_todo_list.incomplete() == []

"""
When a TodoList instance is created complete returns an empty list
"""
def test_complete_empty_list():
    my_todo_list = TodoList()
    assert my_todo_list.complete() == []
