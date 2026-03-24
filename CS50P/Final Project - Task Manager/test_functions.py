import pytest
from functions import Task, add_tasks, completed

def test_invalid_priority():
    with pytest.raises(ValueError):
        Task(title="Test", priority="urgent", due_date="")

def test_invalid_date():
    with pytest.raises(ValueError):
        Task(title="Test", priority="low", due_date="23-03-2026")

def test_empty_title():
    with pytest.raises(ValueError):
        Task(title="", priority="low", due_date="")