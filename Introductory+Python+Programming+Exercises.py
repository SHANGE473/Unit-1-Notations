
# coding: utf-8

# # DICE ROLL

# In[1]:


import random
repeat = True
while repeat:
    print("You rolled",random.randint(1,6))
    print("Do you want to roll again? Y/N")
    repeat = "Y" in input()


# # WEATHER

# In[5]:


weather = float(input("What is the current temperature?"))
if weather > 17:
    print("You should probably wear something a little light.")
    print("but knowing British weather, you should probably take a coat with you, just incase!")
elif weather < 10 and weather > 0:
    print("Dress in layers, coat, scarf, gloves etc.")
elif weather < 0:
    print("Looks like you should stay in, but if you must, be sure to wrap up fully")
elif weather > -10:
    print("I have no idea what you're going to wear!")


# # SW DEVELOPMENT: MINI-MINI PROJECT

# PLAN:
# 
# Requirements:
# User input the number of A levels they did
# Program output the highest degree they can receive from going to uni(diploma, bachelors, masters, etc)
# User input what A levels they did
# Program output what degrees they can do depending on the tier of grading they achieved in each A level
# 
# DESIGN:
# 
# 
# 
# DEVELOPMENT & UNIT TESTING:
# 
# 
# TESTING:
# 
# 
# EVALUATION:

# In[ ]:


no. of Alevel = int(input("How many Alevel did you achieve?"))
if no. of Alevel > 3:
    print("You are eligible for any course up to: ")
if no. of Alevel < 2:
    print("You are eligible to do a HNC or HND, higher national qualification/diploma")


# In[ ]:


age = int(input("what is your age?"))
if age > 17:
    print("You may enter the theatre")
adult = True(input("Are you accompanied by an adult? Y/N"))

