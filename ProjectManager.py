#!/usr/bin/env python
# coding: utf-8

# In[14]:


projects = {}
tasks = []

while True:
    menu = {1:"Add new project", 2:"Show tasks for specific project", 3:"Add task for specific project", 4:"show all projects"}
    print(menu)
    
    
    
    op = int(input("Enter what do you want to do: ")) #Option
    
    if op == 1:
        while True:
            name = input("Please, enter the name of your project: ")
            numOfTasks = int(input("How many tasks do this project have? "))
        
        
            for i in range(numOfTasks):
                t = input("please, enter the Task: ")
                tasks.append(t)
        
            projects[name] = tasks
            tasks = []
            choice = input("\n Do you want to add a new project 'y' or 'n': ")
            if choice == 'n':
                print("\n Done")
                break
        
    elif op == 2:
        p = input("Please, enter the name of the project: ") #Project name
        show = projects.get(p) #Tasks
        print(show)
        
    elif op == 3:
        pr = input("Please, enter the name of the project: ") #Project name
        t = projects.get(p) #Tasks
        
        newTask = input("Please, add the new task you have")
        t.append(newTask)
        projects[pr] = t
        
        print("\n Done")
        
    elif op == 4:
        print(projects)
        
    else:
        print("Please, insert a correct number")
    
    choice = input("\n Do you want to continue 'y' or 'n': ")
    if choice == 'n':
        print("Done")
        break 
    


# In[ ]:




