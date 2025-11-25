import heapq

pq = []

def add_task():
    priority = int(input("Please enter the priority level of this task:     "))
    description = input("Please enter the description of this task: ")
    new_task =(priority, description) #create the new task as a tuple
    heapq.heappush(pq, new_task) #this ensures that when we add a new task, the list pq remains a minimum heap
    print(f"Your task with a priority of {priority} and description of {description} has been succesfully added to your schedule!")

def process_task():
    if pq:
        completed_task = heapq.heappop(pq) #This pops the highest-priority task while keeping our pq a minimum heaep
        print(f"Your task {completed_task[1]}, with a priority of {completed_task[0]} has been completed!")
    else:
        print("Your schedule has no tasks in it.")

def peek_next_task():
    if pq:
        print(f"The next task in your schedule has a priority of {heapq.nsmallest(1, pq)[0][0]} and has the description: {heapq.nsmallest(1,pq)[0][1]}.")
    else:
        print("Your schedule has no tasks in it.")

def print_entire_list():
    for task in pq:
        print(task)

while(True):
    answer = int(input("\n\nSelect one of the following options.\n" \
    "1. Create a new task for your schedule.\n" \
    "2. Complete the next highest-priority task.\n" \
    "3. See (but not complete) the next highest-priority task.\n" \
    "4. Exit program.\n"
    "5. Print the entire list of tasks (this won't be printed necessarily in the order of priority)\n."))
    if answer == 1:
        add_task()
    elif answer == 2:
        process_task() 
    elif answer ==3:
        peek_next_task()
    elif answer == 4:
        break
    elif answer == 5:
        print_entire_list()
    else:
        print("Invalid input. Please try again.")
