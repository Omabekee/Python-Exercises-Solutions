#!/usr/bin/env python
# coding: utf-8

# In[2]:


#3 QUARTER OF THE YEAR

#Ask user to enter month between number 1 and 12
month = int(input("Enter a number (between 1 and 12): "))

#Check quarter of the month
if 1 <= month <= 3:
    print("The month is in the first quarter")
elif 4 <= month <= 6:
    print("The month is in the second quarter")
elif 7 <= month <= 9:
    print("The month is in the third quarter")
elif 10 <= month <= 12:
    print("The month is in the fourth quarter")
else:
    print("Invalid entry. Please enter a valid number (between 1 and 12)")    


# In[ ]:




