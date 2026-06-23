#To Do List Manager
task = []

#Selected Task
def select_task():
    global task
    insert_task = input("Enter a task: ")
    task.append(insert_task)
    
#View Task
def view_task():
    print(task)

#Remove Task
def remove_task():
    global task
    try:
        task_number = int(input("insert task number: "))
        task.pop(task_number - 1)
    except ValueError:
        print("Please insert a number")

#Display Menus
def main():
    while True:
        try:
            print("\n===== Display Menu =====")
            print("1. Add Task")
            print("2. View Task")
            print("3. Remove Task")
            print("4. Exit")
            
            choose = int(input("Choose: "))
            
            if choose == 1:
                select_task()
            elif choose == 2:
                view_task()
            elif choose == 3:
                remove_task()
            elif choose == 4:
                break
            else:
                print("Please enter number 1-4")
                
        except:
            print("Invalid number")
            
main()