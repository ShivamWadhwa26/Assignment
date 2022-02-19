#!/usr/bin/env python
# coding: utf-8

# Write a Python Program to Check if a Number is Positive, Negative or Zero?

# In[1]:


def check(x):
    if x==0:
        print("Number is zero")
    elif x>0:
        print("Number is positive")
    else:
        print("Number is negative")
        
check(int(input("Enter a no.:")))


# Write a Python Program to Check if a Number is Odd or Even?

# In[2]:


def evenodd(x):
    if x%2==0:
        print("Number is even")
    else:
        print("Number is odd")

evenodd(int(input("Enter a no.:")))


# Write a Python Program to Check Leap Year?

# In[3]:


def leapyear(x):
    if x%4==0:
        print("It is a leap year")
    else:
        print("It is not a leap year")
        
leapyear(int(input("Enter a year:")))


# Write a Python Program to Check Prime Number?

# In[8]:


def isprime(x):
    c=0
    for i in range(1,x+1):
        if x%i==0:
            c=c+1
    if c==2:
        print(x,"is a prime no.")
    else:
        print(x,"is not a prime no.")
        
isprime(int(input("Enter a year:")))


# Write a Python Program to Print all Prime Numbers in an Interval of 1-10000?

# In[5]:


def isprime(x):
    c=0
    for i in range(1,x+1):
        if x%i==0:
            c=c+1
    if c==2:
        print(x)

for i in range(1,10001):
    isprime(i)


# In[ ]:





# In[ ]:




