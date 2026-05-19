print("--- Student To-Do List ---")

tasks = []

while True:
    print("\n1. Add Task  |  2. Show Tasks  |  3. Exit")
    choice = input("Choose an option (1-3): ")
    
    if choice == '1':
        task = input("Enter the task: ")
        tasks.append(task)
        print(f"'{task}' added successfully!")
    elif choice == '2':
        if not tasks:
            print("Your list is empty!")
        else:
            print("\nYour Current Tasks:")
            for index, item in enumerate(tasks, start=1):
                print(f"{index}. {item}")
    elif choice == '3':
        print("Good luck with your studies!")
        break
    else:
        print("Invalid choice! Please choose 1, 2, or 3.")
