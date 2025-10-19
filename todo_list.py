tasks = []
while True:
    command = input("What would  you to do? (add, view, quit): ")
    if command == "quit":
        print("Goodbye!")
        break
    elif command == "add":
        new_task = input("What task would you like to add? ")
        tasks.append(new_task)
    elif command == "view":
        if not tasks:
            print("Your to do list is empty")
        else:
            for index, item in enumerate(tasks):
                print(f"{index+1}. {item}")
    elif command == "remove":
        if not tasks:
            print("Your to do list is empty")
        else:
            for index, item in enumerate(tasks):
                print(f"{index+1}. {item}")
            try:
                removable_tasks = input("Enter the task number to remove :")
                removable_tasks = int(removable_tasks)
                if 1 <= removable_tasks <= len(tasks):
                    # Convert to a 0-based index and remove the item.
                    index_to_remove = removable_tasks - 1
                    removed_task = tasks.pop(index_to_remove)
                    print(f"✅ Removed task: '{removed_task}'")
                else:
                    # This handles numbers that are too high or too low.
                    print("❌ Invalid task number.")
            except ValueError:
                print("Please, Enter a valid number")

    else:
        print("Unknown command")
    

