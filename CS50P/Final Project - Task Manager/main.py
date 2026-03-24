import functions

def main():
    while True:
        print("\n1. Add task")
        print("2. Complete task")
        print("3. List tasks")
        print("4. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            task = functions.get_task()
            functions.add_tasks(task)
        elif choice == "2":
            title = input("Task title: ").strip()
            functions.completed(title)
        elif choice == "3":
            functions.list_tasks()
        elif choice == "4":
            break
        else:
            print("Invalid option")
    


if __name__ == "__main__":
    main()