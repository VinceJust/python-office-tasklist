# tasklist variable with empty array
tasklist = []

# defining function for adding tasks
def add_task():
    task = input("Bitte gib eine Aufgabe ein, die in deiner Aufgabenliste hinzugefügt werden soll: ")
    due_date = input("Gib das Fälligkeitsdatum an: ")
    task_with_due = {"task": task, "due_date": due_date}
    tasklist.append(task_with_due)
    print(f"Aufgabe '{task}' wurde zur Liste hinzugefügt.")


# testing the function
add_task()
