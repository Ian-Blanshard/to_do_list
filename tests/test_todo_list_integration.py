from lib.todo import *
from lib.todo_list import *


"""
When a TodoList instance is created and an todo instance is added
incomplete returns a list containing the tasks
"""
def test_incompleted_single_entry():
    my_todo_list = TodoList()
    todo_one = Todo('Washing up')
    my_todo_list.add(todo_one)
    result = my_todo_list.incomplete()
    assert result == [todo_one]

"""
When a TodoList instance is created and multiple todo instances are added
incomplete returns a list containing the tasks
"""
def test_incompleted_multiple_entries():
    my_todo_list = TodoList()
    todo_one = Todo('Washing up')
    todo_two = Todo('Hoovering')
    my_todo_list.add(todo_one)
    my_todo_list.add(todo_two)
    result = my_todo_list.incomplete()
    assert result == [todo_one, todo_two]

"""
When a Todo list instance is created and completed incomplete returns a empty list
ans complete returns a list containing the todo instance
"""
def test_completed_single_entry():
    my_todo_list = TodoList()
    todo_one = Todo('Washing up')
    my_todo_list.add(todo_one)
    todo_one.mark_complete()
    incomplete_result = my_todo_list.incomplete()
    assert incomplete_result == []
    complete_result = my_todo_list.complete()
    assert complete_result == [todo_one]

"""
When multiple Todo list instances are created and  one completed incomplete and
complete return the correct instances 
"""
def test_completed_single_entry_incomplete_single_entry():
    my_todo_list = TodoList()
    todo_one = Todo('Washing up')
    todo_two = Todo('Hoovering')
    my_todo_list.add(todo_one)
    my_todo_list.add(todo_two)
    todo_one.mark_complete()
    incomplete_result = my_todo_list.incomplete()
    assert incomplete_result == [todo_two]
    complete_result = my_todo_list.complete()
    assert complete_result == [todo_one]

"""
When multiple Todo list instances are created and give up is used
all instances are marked as complete 
"""
def test_give_up_marks_all_complete():
    my_todo_list = TodoList()
    todo_one = Todo('Washing up')
    todo_two = Todo('Hoovering')
    my_todo_list.add(todo_one)
    my_todo_list.add(todo_two)
    my_todo_list.give_up()
    incomplete_result = my_todo_list.incomplete()
    assert incomplete_result == []
    complete_result = my_todo_list.complete()
    assert complete_result == [todo_one, todo_two]

