from collections import deque

q = deque()

while(True):
    answer = int(input("\n\nChoose anumber between 1-4 to select an option:\n" \
    "1. Add customer to queue.\n" \
    "2. Serve the next customer.\n" \
    "3. View the current queue.\n" \
    "4. Exit the program.\n"))
    if answer == 1: 
        name = input("Enter the name of the customer that you want to add to the queue: ")
        q.append(name)
        print(f"{name} was succesfully added to the queue.")
    elif answer == 2:
            try: 
                satisfied_customer = q.popleft() 
            except Exception:
                 print("Your queue is empty. Can't do a popleft.")
            else:
                 print(f"{satisfied_customer} was served.")
    elif answer == 3:
         print(f"This is the current quque: {q}")
    elif answer == 4:
         print("Exiting program. Goodbye!")
         break
    else:
         print("Invalid input.")