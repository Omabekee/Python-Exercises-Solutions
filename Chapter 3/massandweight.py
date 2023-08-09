#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#5 MASS AND WEIGHT

#Ask user to enter object's mass

mass = float(input("Enter the mass of the object: "))
weight = mass * 9.8

print("The weight of the object is", weight, "newtons")

#Check if weight is heavy or light
if weight > 500:
    print("Object is too heavy")
elif weight < 100:
    print("Object is too light")

