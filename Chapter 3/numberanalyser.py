#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1 NUMBER ANALYSER

#Ask the user to enter a string and check if the string contains only digit

ent_str = input("Enter an integer: ")

if ent_str.isdigit():
    num = int(ent_str) #this code converts the valid string to an integer and assigns it to 'num' variable.
    
    #Check if the number is positive, negative or zero
    if num > 0:
        print("Positive")
    elif num < 0:
        print("Negative")
    else:
        print("Zero")
            
    #Check if the number is Even or Odd
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")
        
#Always take not of the indentation- if the first "if" statement is false, it displays the error message below.         
else:
    print("Invalid input. Please enter a valid integer")
    
    


# In[ ]:




