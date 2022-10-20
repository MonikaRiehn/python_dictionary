#!/usr/bin/env python
# coding: utf-8

# # built-in functions

# In[1]:


# function stores and reuses code. it takes some input, runs the steps in the function
# and produces an output
def thing():
    print('Hello')
    print('Mom')
thing()
print('oops')
thing()


# In[2]:


# built-in functions come with python: input(), type(), float(), inter()
# function we define ourselves
# assignment = function('argument')


# In[4]:


# max function prints highest value, in this case biggest letter in the string
big = max('Hello world')
print(big)

# min function returns lowest value (here blank)
tiny = min('Hello world')
print(tiny)


# In[7]:


# type conversions are functions: int() and float()
print(float(99)/100)


# In[8]:


i = 46
type(i)


# In[9]:


f = float(i)
print(f)


# In[10]:


type(f)


# In[12]:


print(1 + 2 * float(3) / 4 - 5)


# In[14]:


# string conversions:
sval = '123'
type(sval)


# In[18]:


ival = int(sval)
print(type(ival))
print(ival+1)


# # create our own functions

# In[21]:


# def: store
def print_dogs ():
    print('Dachshund')
    print('Pitbull')
# invoke: call
print_dogs()


# In[22]:


# argument: value we pass into the function as its input when calling function
# enables function to do different kinds of work
# place in () after name of function
# big = max ('Hello World')


# In[24]:


# PARAMETERS
# variable used in the function definition
# placeholder/handle that allows code in function to access arguments for
# particular function invocation
# parameter here is (lang). like a container/alias for later input.
def greet(lang):
    if lang == 'es':
        print('Hola')
    elif lang == 'fr':
        print('Bonjour')
    else:
        print('Hello')


# In[25]:


greet('en')


# In[26]:


greet('fr')


# In[27]:


greet('es')


# In[28]:


# RETURN VALUES
# "return" keyword: function takes its arguments, computes something and returns a value
# to be used as value of the function call in the calling expression.
def greet():
    return 'Hello'
print(greet(), 'Mom')
print(greet(), 'Dad')


# In[29]:


def greet(lang):
    if lang == 'es':
        return 'Hola'
    elif lang == 'fr':
        return 'Bonjour'
    else:
        return 'Hello'


# In[32]:


print(greet('en'), 'Mom')
print(greet('fr'), 'Croissant')
print(greet('es'), 'Espanol')


# In[34]:


# multiple parameters/arguments
def addtwo(a,b):
    added = a + b
    return added
x = addtwo(4,3)
print(x)


# # Exercise
# Code from last exercise:

# In[39]:


sh = input('Enter hours: ')
sr = input('Enter rate: ')

try:
    fh = float(sh) #DANGER ZONE
    fr = float(sr) #DANGER ZONE
except:
    print('Error, please enter a numeric input!')
    quit() # do not continue!
  
if fh > 40:
    print('Overtime')
    reg = fr * fh
    otp = (fh - 40) * (fr * 0.5)
    print(f'regular payment + {reg} + overtime payment {otp}')
    xp = reg + otp
else:
    print('Regular')
    xp = fh * fr

print(f'Pay: {xp}')


# This time with a function:

# In[47]:


def computepay(hours, rate):
    if hours > 40:
        print('Overtime')
        reg = rate * hours
        otp = (hours - 40) * (rate * 0.5)
        pay = reg + otp
    else:
        print('Regular')
        pay = hours * rate
    return pay
# "return" is the result/value of what the function has computed with the parameters.
# when funcion is called later, the "return"-value is assigned to the variable, which is
# to be printed at the end.

sh = input('Enter hours: ')
sr = input('Enter rate: ')

try:
    fh = float(sh) #DANGER ZONE
    fr = float(sr) #DANGER ZONE
except:
    print('Error, please enter a numeric input!')
    quit()

# sends back fh and fr to function above and computes them as hours and rates.
# the value of the "return pay" is then assigned to xp.
xp = computepay(fh, fr)

print('Pay: ', xp)


# In[ ]:




