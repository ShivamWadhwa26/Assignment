#!/usr/bin/env python
# coding: utf-8

# Q) Write a Python program to convert kilometers to miles?

# In[1]:


#1km= 0.62137 miles
def kmintomiles():
    km=float(input("enter distance in kilometers:"))
    print(km,"km is equal to",0.62137*km,"miles")

kmintomiles()


# Q) Write a Python program to convert Celsius to Fahrenheit?

# In[2]:


def coverttemp():
    temp=int(input("enter temp in celsius:"))
    print(temp,"Celsius is equal to",((9/5)*temp)+32,"Fahrenheit")
    
coverttemp()


# Write a Python program to display calendar?

# In[3]:


def calendar():
    import calendar
    yy=int(input("Enter year:"))
    mm=int(input("Enter month in digits(1-12):"))
    print(calendar.month(yy, mm))


calendar()


# Write a Python program to solve quadratic equation?

# In[9]:


import math 

def equationroots(): 
    a=int(input("Enter value of a:"))
    b=int(input("Enter value of b:"))
    c=int(input("Enter value of c:"))
    # calculating discriminant using formula
    discriminant = b * b - 4 * a * c 
    sqrt_discriminant = math.sqrt(abs(discriminant)) 
      
    # checking condition for discriminant
    if discriminant > 0: 
        print("real roots:") 
        print((-b + sqrt_discriminant)/(2 * a)) 
        print((-b - sqrt_discriminant)/(2 * a)) 
      
    elif discriminant == 0: 
        print("real and same roots:") 
        print(-b / (2 * a)) 
      
    # when discriminant is less than 0
    else:
        print("Complex Roots") 
        print(- b / (2 * a), " + i", sqrt_discriminant) 
        print(- b / (2 * a), " - i", sqrt_discriminant)
        
equationroots()    


# Write a Python program to swap two variables without temp variable?

# In[11]:


def swap(a,b):
    print("before swapping value of a:",a,"b:",b)
    a,b=b,a
    print("after swapping value of a:",a,"b:",b)

swap(1,2)


# In[ ]:





# In[ ]:




