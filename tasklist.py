# tasklist variable with empty array
tasklist = []

# defining function for adding tasks
def add_task():
    task = input("Bitte gib eine Aufgabe ein, die in deiner Aufgabenliste hinzugefügt werden soll: ")
    due_date = input("Gib das Fälligkeitsdatum an: ")
    task_with_due = {"task": task, "due_date": due_date}
    tasklist.append(task_with_due)
    print(f"Aufgabe '{task}' wurde zur Liste hinzugefügt.")



# defining function for showing the task list
def show_tasklist():
    if not tasklist: # checks if list is empty
        print("Deine Aufgabenliste ist leer.")
    else:
        print("Deine Aufgabenliste:")
        for idx, task in enumerate(tasklist, start=1): # generates index starting from 1
            print(f"{idx}. Aufgabe: {task['task']} - Fälligkeitsdatum: {task['due_date']}")

# function test
add_task()
show_tasklist()

