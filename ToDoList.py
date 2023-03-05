import time

toDoList = []

t = 2
def add_task(toDoList):
    task = input("please enter task:")
    toDoList.append(task)
    print("Saved succesfully...")
    time.sleep(t)

def del_task(toDoList):
    cell = int(input("select the task you want to delete:"))


    choose = input("Are you sure to delete? Y or N")
    time.sleep(t)
    if(choose == 'Y' or choose == 'y'):
        toDoList.pop(cell)

        print("Delete is succesfull!")
        time.sleep(t)
    elif(choose == 'N' or choose == 'n'):
        print("deletion aborted")
        time.sleep(t)



def show_task(toDoList):
    print("tasks to be done: ")
    for task in toDoList:
        print("- ",task)

def marking(toDoList):
    try:
        temp = ""
        sign = int(input("Which tasks would you like to mark as 'done'?"))
        temp = toDoList[sign]
        toDoList.pop(sign)
        temp2 = temp + '   X'
        toDoList.append((temp2))

    except IndexError:
        print("No task found at this number")




while True:

    print("""
    TO DO LIST APP
    
    1.ADD TASK
    2.SHOW TASKS
    3.DELETE TASK
    4.MARKING TASK
    5.QUIT
    """)

    choice = input("Enter: 1/2/3/4/5")

    if(choice == "1"):
        add_task(toDoList)
    elif(choice == "2"):
        show_task(toDoList)
    elif(choice == "3"):
        del_task(toDoList)
    elif(choice == "4"):
        marking(toDoList)
        show_task(toDoList)
    elif(choice == "5"):
        print("quit...")
        time.sleep(1)
        break
