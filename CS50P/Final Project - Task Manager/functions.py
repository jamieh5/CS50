import csv
import os
from datetime import datetime

class Task():
    def __init__(self, title, priority, due_date, status="Incompleted"):
        if not title.strip():
            raise ValueError("No title")
        if priority not in ["low", "medium", "high"]:
            raise ValueError("Wrong priority set")
        if due_date:
            try:
                datetime.strptime(due_date, "%Y-%m-%d")
            except ValueError:
                raise ValueError("Invalid date format, use YYYY-MM-DD")

        self.title = title
        self.due_date = due_date
        self.priority = priority
        self.status = status
        self.created_at = datetime.now().strftime("%Y-%m-%d")

    def to_dict(self):
        return {
            "title": self.title,
            "due_date": self.due_date or "Today",
            "priority": self.priority,
            "status": self.status,
            "created_at": self.created_at
        }

def get_task():
    title = input("Title: ")
    priority = input("Priority: ")
    due_date = input("Due date: ")
    return Task(title=title, priority=priority, due_date=due_date)

def add_tasks(task):
    with open("tasks.csv", "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["title", "due_date", "priority", "status", "created_at"])
        writer.writerow(task.to_dict())

def delete_tasks():
    ...

def change_priority():
    ...

def completed():
    ...

def list_tasks():
   ...