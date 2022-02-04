#!/usr/bin/env python
# coding: utf-8

# In[2]:


# #this is the simple calcularot that takes tow numbers and make the main operations for them(+, -, *, /)
# firstNum = int(input("Please, insert the first number"))
# secondNum = int(input("Please, insert the second number"))

# print("The summation of ", firstNum, " + ", secondNum, " = " , firstNum+secondNum, 
#       "\n the subtraction of ", firstNum, " - ", secondNum, " = " , firstNum-secondNum, 
#       "\n the multiplication of ", firstNum, " * ", secondNum, " = " , firstNum*secondNum, 
#       "\n the divition of ", firstNum, " \ ", secondNum, " = " , firstNum/secondNum)


# In[4]:


#update the code
#This code is updated version for simple calculator 

firstNum = int(input("Please, insert the first number"))
secondNum = int(input("Please, insert the second number"))

def addition(num1,num2):
    print(num1 + num2)

def subtraction(num1,num2):
    print(num1 - num2)

def multiplication(num1,num2):
    print(num1 * num2)

def division(num1,num2):
    print(num1 / num2)

while True:
    choose = int(input("Please choose from the menu: "
                      "\n 1- Addition"
                      "\n 2- Subtraction"
                      "\n 3- Multiplication"
                      "\n 4- Divition"
                      "\n 5- Exit"))
    if choose == 1:
        addition(firstNum,secondNum)
    elif choose == 2:
        subtraction(firstNum,secondNum)
    elif choose == 3:
        multiplication(firstNum,secondNum)
    elif choose == 4:
        divition(firstNum,secondNum)
    elif choose == 5:
        print("Thank you for using my Calculator")
        break
    else:
        print("Please, choose the correct number")


# In[ ]:




