#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np


# In[ ]:


#disclaimer: I have never coded before LOL I am SO sorry for how elementary this is :(


# In[16]:


#A list of foods served by the school cafeteria
Foods = ["pizza", "tacos", "sushi", "cookies"]

#A list of dictionaries
Favoritefoods = [{'name':'Bob','food':'pizza'}, {'name':'Jake','food':'tacos'}, {'name':'Luke','food':'sushi'}, {'name':'Tara','food':'cookies'}]


# In[42]:


print("What is your favorite food?")
x = input()

def IsItInCafeteria(x,Foods):
    if (x in Foods):
        print("Your favorite food is " +  x + "!" + " Very cool, the school cafeteria has this!")
    else:
        print(" The school cafeteria does not serve this!")

IsItInCafeteria(x,Foods)


# In[36]:


arr = np.array([Foods])
print("In alphabetical order, the cafeteria serves", np.sort(arr))


# In[37]:


print(Favoritefoods[0]['name'], "always orders", Favoritefoods[0]['food'], "from the cafeteria.")

