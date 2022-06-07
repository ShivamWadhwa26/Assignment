#!/usr/bin/env python
# coding: utf-8

# # Solution 1

# In[1]:


def read_replace_file(path,replace_content,replace_with):
    """
    A Python program to read a file and replace a content with another content
    path: path of the text file
    replace_content: word need to replace
    replace_with: replacement of the word
    
    Example:
    path='example.txt',replace_content='placement',replace_with='screening'
    original content: This is a placement assignment
    output: This is a screening assignment
    """
    
    #To read the file and form a new string with replaced content
    with open(path, "r") as f:
            for x in f:
                l=str(x).split(' ')
            k=l.index(replace_content)
            l[k]=replace_with
            newData=' '.join(l)
            
    #To overwrite the file with new content
    with open(path, "w") as f:
        f.write(newData)
    
    #To read the final content
    with open(path, "r") as f:
        print(f.read())


# In[2]:


read_replace_file('example.txt',replace_content='placement',replace_with='screening')


# # Solution 2

# ## Abstract Class

# An abstract class is a blueprint for other classes. It allows us to create a set of methods that must be created within any child classes built from the abstract class. A class which contains one or more abstract methods is called an abstract class.

# In[3]:


from abc import ABC, abstractmethod

class smartphone(ABC):
    @abstractmethod
    def camera(self):
        pass
    
class iphone13(smartphone):
    def camera(self):
        print("The camera of iPhone 13 is 12 megapixels")
        
class samsungs22(smartphone):
    def camera(self):
        print("The camera of Samsung S22 is 108 megapixels")
    
class oneplus10(smartphone):
    def camera(self):
        print("The camera of OnePlus 10 is 48 megapixels")

a = iphone13()
a.camera()

b = samsungs22()
b.camera()

c = oneplus10()
c.camera()


# ## Multiple Inheritence

# In multiple inheritance, the features of all the base classes are inherited into the derived class.

# In[4]:


#Syntax for multi-class Inheritence
class Base1:
    pass

class Base2:
    pass

class MultiDerived(Base1, Base2):
    pass

#Syntax for multi-level Inheritence
class Base1:
    pass

class Derived(Base1):
    pass

class Derived1(Derived):
    pass


# In[5]:


#Example of multi-level Inheritence
class ABC:
    
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    
    def test(self):
        print("This is a test method of class ABC")
        
class ABC1(ABC):
        
    def test1(self):
        print("This is a test1 method of class ABC1")
        
class ABC2(ABC1):
    
    def test2(self):
        print("This is test2 method of class ABC2")

class ABC3(ABC2):
    
    def test3(self):
        print("This is test3 method of class ABC3") 


# In[6]:


m = ABC3(1,2,3)


# In[7]:


m.test3()


# In[8]:


#Example of multi-class Inheritence
class ABC:
    
    def __init__(self,p,q,r):
        self.p = p
        self.q = q
        self.r = r
    
    def test(self):
        print("This is a test method of class ABC")
        
class ABC1:
    
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
        
    def test1(self):
        print("This is a test1 method of class ABC1")

class child(ABC1,ABC):
    
    def __init__(self,*args,**kwargs):
        ABC.__init__(self,*args)
        ABC1.__init__(self,**kwargs)


x = child(9,4,3,a=2,b=6,c=4)


# In[9]:


x.b


# In[10]:


x.p


# ## Decorators

# It allows programmers to modify the behaviour of function or class. Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function, without permanently modifying it.

# In[11]:


def func_needs_decorator():
    print("This function is in need of a Decorator")


# In[12]:


func_needs_decorator()


# In[13]:


def new_decorator(func):

    def wrap_func():
        print("Code would be here, before executing the func")

        func()

        print("Code here will execute after the func()")

    return wrap_func

def func_needs_decorator():
    print("This function is in need of a Decorator")


# In[14]:


@new_decorator
def func_needs_decorator():
    print("This function is in need of a Decorator")


# In[15]:


func_needs_decorator()


# A decorator simply wrapped the function and modified its behavior.
# ---------------------------------------------------------------------------------------------------------
# Use Case: In the following example we are using @app.route decorator to form the api of code
# 
# 
# from flask import Flask, request, jsonify
# 
# app = Flask(__name__)
# 
# @app.route('/xyz',methods=['GET','POST'])
# def test():
#     if(request.method=='POST'):
#         a=request.json['num1']
#         b=request.json['num2']
#         result = a+b
#         return jsonify(str(result))
# 
# if __name__=='__main__':
#     app.run()
