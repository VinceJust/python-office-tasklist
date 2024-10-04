# tasklist variable with empty array
tasklist = []

# defining function for adding tasks
def add_task():
    task = input("Bitte gib eine Aufgabe ein, die in deiner Aufgabenliste hinzugefügt werden soll: ") # prompt user to enter task
    due_date = input("Gib das Fälligkeitsdatum an: ") # prompt user to enter due date
    task_with_due = {"task": task, "due_date": due_date}
    tasklist.append(task_with_due) # append task disctionary to task list
    print(f"Aufgabe '{task}' wurde zur Liste hinzugefügt.") # confirm tasks has been added



# defining function for showing the task list
def show_tasklist():
    if not tasklist: # checks if list is empty
        print("Deine Aufgabenliste ist leer.")
    else:
        print("Deine Aufgabenliste:")
        for idx, task in enumerate(tasklist, start=1): # generates index starting from 1
            print(f"{idx}. Aufgabe: {task['task']} - Fälligkeitsdatum: {task['due_date']}")


# defining function to delete tasks
def remove_task():
    show_tasklist() # show current tasks of user
    if tasklist: # check if there are tasks to delete
        try:
            task_index = int(input("Gib die Nummer der Aufgabe ein die du entfernen möchtest: ")) - 1
            if 0 <= task_index < len(tasklist):
                remove_task = tasklist.pop(task_index)
                print(f"Aufgabe '{remove_task['task']}' wurde entfernt.")
            else:
                print("Ungültige Nummer. Bitte versuche es erneut.")
        except ValueError:
            print("Bitte gib eine gültige Zahl ein.")





# defining main function
def main():
    while True:
        # display options for user
        print("\nWas möchtest du tun?")
        print("1. Aufgabe hinzufügen")
        print("2. Aufgabeliste anzeigen")
        print("3. Aufgabenliste entfernen")
        print("4. Programm beenden")
        
        # prompt for user to select option
        choice = input ("Bitte wähle eine Option (1-4): ")

        # process of user's choice
        if choice == '1':
            add_task()
        elif choice == '2':
            show_tasklist()
        elif choice == '3':
            remove_task()
        elif choice == '4':
            print("Programm wird beendet.")
            break
        else:
            print("Ungültige Eingabe. Bitte wähle eine gültige Option.")

# automatic run function (not quite sure how it works)
if __name__ == "__main__":
    main()            


