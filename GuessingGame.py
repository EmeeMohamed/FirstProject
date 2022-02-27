#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random 



print("Guss The Number")

while True:
    rand = random.randint(1,10)
    print("You can Try 3 times")
    
    for i in range(3):
        num = int(input("Insert a number between 1 to 10: "))
        if num > rand:
            print("Your number is bigger, Try again! ")
        elif num < rand:
            print("Your number is smaller, Try again! ")
        elif num == rand:
            print("Correct Answer, YOU WIN ^__^ ")
            break
        else:
            print("Insert the correct number")
            
            
    choice = input("\n Do you want to play again 'y' or 'n': ")
    if choice == 'n':
        print("Thanks for playing")
        break 


# In[ ]:




