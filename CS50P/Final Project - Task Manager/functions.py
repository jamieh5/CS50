import csv
from datetime import datetime
from tabulate import tabulate

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

def completed(title):
    with open("tasks.csv") as file:
        reader = csv.DictReader(file, skipinitialspace=True)
        rows = list(reader)

    found = False
    for row in rows:
        if row["title"] == title:
            row["status"] = "Completed"
            found = True

    if  not found:
        raise ValueError("Wrong Title")

    with open("tasks.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["title", "due_date", "priority", "status", "created_at"])
        writer.writeheader()
        writer.writerows(rows)

def list_tasks():
    data = []
    with open("tasks.csv") as file:
       reader = csv.DictReader(file, skipinitialspace=True)
       for row in reader:
           data.append(row)
    print(tabulate(data[1:], data[0], tablefmt="grid"))