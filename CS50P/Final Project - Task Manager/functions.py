import csv
from datetime import datetime

class Task():
    def __init__(self, title, priority, status="Incomplete", id=None, due_date=None):
        if not title.strip():
            raise ValueError("No title")
        if priority not in ["low", "medium", "high"]:
            raise ValueError("Wrong priority set")
        if due_date:
            try:
                datetime.strptime(due_date, "%Y-%m-%d")
            except ValueError:
                raise ValueError("Invalid date format, use YYYY-MM-DD")

        self.id = id
        self.title = title
        self.due_date = due_date
        self.priority = priority
        self.status = status
        self.created_at = datetime.now().strftime("%Y-%m-%d")

def get_task():
    title = input("Title: ")
    priority = input("Priority: ")
    due_date = input("Due date: ")
    return Task(title=title, priority=priority, due_date=due_date)

def add_tasks():
    ...

def delete_tasks():
    ...

def change_priority():
    ...

def completed():
    ...

def list_tasks():
   ...