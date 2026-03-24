# Task Manager

A command-line task manager that stores tasks in a CSV file.

## Description

A Python program that allows you to manage your daily tasks from the terminal.
Tasks are saved in a CSV file so they persist between sessions.

## Features

- Add tasks with title, priority, and due date
- Mark tasks as completed
- List all tasks in a formatted table

## Usage

Run the program with:
python project.py

Then choose from the menu:

1. Add task - Add a new task with title, priority (low/medium/high), and optional due date (YYYY-MM-DD)
2. Complete task - Mark a task as completed by entering its title
3. List tasks - Display all tasks in a table
4. Exit - Exit the program

## Dependencies

Install required libraries with:
pip install tabulate
