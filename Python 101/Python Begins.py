#!/usr/bin/env python
# coding: utf-8

# In[4]:


print('Hello World!')


# # First Notebook!

# In[ ]:





# # Variables in Python

# In[1]:


x = 22

print(x)


# In[2]:


print(x)


# In[3]:


type(x)


# In[4]:


y = 'Mint Chocolate Chip'

print(y)


# In[5]:


type(y)


# In[7]:


print(y)


# In[8]:


x,y,z = 'Chocolate', 'Vanilla', 'Rocky Road'


# In[9]:


print(x)
print(y)
print(z)


# In[10]:


x = y = z = 'Root Beer Float'

print(x)
print(y)
print(z)


# # LIST

# In[11]:


ice_cream = ['Chocolate', 'Vanilla', 'Rocky Road']
x,y,z = ice_cream

print(x)
print(y)
print(z)


#  # Naming Variables
#  

# In[ ]:


# Camel Case

# Test Variable Case

testVariableCase = 'Vanilla Swirl'


# In[ ]:


# Pascal Case

# Test Variable Case

TestVariableCase = 'Vanilla Swirl'


# In[ ]:


# Snake Case

# Test Variable Case

test_variable_case = 'Vanilla Swirl'


# In[ ]:





# In[12]:


testvar = 'Vanilla Swirl'
test_var = 'Vanilla Swirl'
_test_var = 'Vanilla Swirl'
testVar = 'Vanilla Swirl'
TestVar = 'Vanilla Swirl'
TestVar2 = 'Vanilla Swirl'


# In[ ]:


This is wrong!
2TestVar = 'Vanilla Swirl'
Test-Var2 = 'Vanilla Swirl'
Test Var2 = 'Vanilla Swirl'
Test,Var2 = 'Vanilla Swirl'


# In[13]:


x = 'Ice Cream is my favorite' + '.'

print(x)


# In[14]:


y = 3 + 2

print(y)


# In[16]:


x = 'Ice Cream'
y = ' is'
z = ' my favorite.'

print(x+y+z)


# In[17]:


x = 1
y = 2
z = 3
print(x+y+z)


# In[18]:


x = 'Ice Cream'
y = 2
print(x,y)


# In[ ]:





# In[ ]:





# # Data Types

# Numeric - integars, float, complex numbers

# In[21]:


type(-12 + 100)


# In[22]:


type(-12 + 10.25)


# In[23]:


type(-12 + 3j)


# Boolean - True or False

# In[25]:


#Boolean
type(True)


# In[26]:


type(False)


# In[27]:


type(1>5)


# In[28]:


1>5


# In[29]:


1==1


# Sequence data types - strings, lists, tuples

# In[30]:


#Strings

'Single Quoate'


# In[31]:


"Double Quote"


# In[33]:


multiline = """
I am currently learning python for the umpth time; but this time around, things are different

"""


# In[34]:


print(multiline)


# In[35]:


type(multiline)


# In[36]:


a = 'Hello World!'


# In[38]:


print(a[6])


# In[39]:


a*3


# In[40]:


#Lists

[1,2,3]


# In[42]:


['cookie', 'strawberry', 'chocolate']


# In[43]:


['Vanilla', 3, ['Scoops', 'spoon'], True]


# In[46]:


Ice_cream = ['cookie', 'strawberry', 'chocolate']

Ice_cream.append('salted caramel')

Ice_cream


# In[47]:


Ice_cream


# In[48]:


Ice_cream[0] = 'Butter Pecan'
Ice_cream


# In[49]:


Nest_list = ['Vanilla', 3, ['Scoops', 'spoon'], True]


# In[54]:


Nest_list[2][1]


# In[ ]:





# In[55]:


#Tuple

tuple_scoops = (1,2,3,2,1)


# In[56]:


type(tuple_scoops)


# In[59]:


tuple_scoops[3]


# # Sets
# 
# 

# In[60]:


daily_pints = {1,2,3}


# In[61]:


type(daily_pints)


# In[62]:


print(daily_pints)


# In[64]:


daily_pints_log = {1,2,31,2,3,4,1,2,5,6,3,2}

print(daily_pints_log)


# In[65]:


wifes_daily_pints_log = {1,3,5,7,3,24,5,7,3,2,0}


# In[66]:


print(daily_pints_log | wifes_daily_pints_log)


# In[67]:


print(daily_pints_log & wifes_daily_pints_log)


# In[68]:


print(daily_pints_log - wifes_daily_pints_log)


# In[69]:


print(daily_pints_log ^ wifes_daily_pints_log)


# # Dictionaries

# In[70]:


#key/value Pair


# In[71]:


dict_cream = {'name':'Joshua Familusi', 'Weekly intake': 5, 'favoriate ice creams': ['MCC', 'Chocolate']}


# In[72]:


type(dict_cream)


# In[73]:


print(dict_cream)


# In[75]:


dict_cream.values()


# In[76]:


dict_cream.keys()


# In[77]:


dict_cream.items()


# In[78]:


dict_cream['name']


# In[79]:


dict_cream['name'] = 'MT Familusi'

print(dict_cream)


# In[83]:


dict_cream.update({'name': 'MT Familusi', 'Weekly intake': 5, 'weight': 300})

print(dict_cream)


# In[87]:


del dict_cream['weight']

print(dict_cream)


# In[84]:





# In[88]:


print(dict_cream)


# In[ ]:





# # Comparison Operators
# 

# In[89]:


10 == 10


# In[90]:


10 == 25


# In[91]:


10 != 25


# In[92]:


'Vanilla' == 25


# In[100]:


x = 'vanlla'
y = 'chocolate'

x != y


# In[101]:


10 <50


# In[102]:


10 <= 10


# # Logical Operators
# 
# and, or, not

# In[103]:


(10 > 50) and (50 > 10)


# In[105]:


(70 > 50) and (50 > 10)


# In[106]:


(10 > 50) or (50 > 10)


# # Membership Operators
# 
# In, Not in

# In[107]:


ice_cream = 'I love chocolate ice cream'

'love' in ice_cream


# In[109]:


scoops = [1,2,3,4,5]
wanted_scoops = 8

6 not in scoops


# In[ ]:





# # If - Elif - Else Statement

# In[110]:


if 25 > 10:
    print('it worked')


# In[112]:


if 25 < 10:
    print('it worked')
else:
    print('it did not work')


# In[113]:


if 25 < 10:
    print('it worked')
elif 25 < 20:
    print('elif worked')
elif 25 < 21:
    print('elif2 worked')
elif 25 < 40:
    print('elif3 worked')
elif 25 < 50:
    print('elif4 worked')
else:
    print('it did not work')


# In[115]:


if (25 < 10) or (1 < 3):
    print('it worked')
elif 25 < 20:
    print('elif worked')
elif 25 < 21:
    print('elif2 worked')
elif 25 < 40:
    print('elif3 worked')
elif 25 < 50:
    print('elif4 worked')
else:
    print('it did not work')


# In[116]:


print('it worked') if 10 > 30 else print('it did not work')


# In[117]:


#Nested If statement


# In[118]:


if (25 < 10) or (1 < 3):
    print('it worked')
    if 10 > 5:
        print('This nested if statement worked!!!')
elif 25 < 20:
    print('elif worked')
elif 25 < 21:
    print('elif2 worked')
elif 25 < 40:
    print('elif3 worked')
elif 25 < 50:
    print('elif4 worked')
else:
    print('it did not work')


# # For Loops

# In[1]:


integers = [1,2,3,4,5]


# In[7]:


for number in integers:
    print('Yeah!')


# In[ ]:


integers = [1,2,3,4,5]


# In[8]:


for Peanut in integers:
    print(Peanut + Peanut)


# In[9]:


#dictionary


# In[10]:


ice_cream_dict = {'name': 'Joshua Familusi', 'weekly intake': 5, 'favorite ice cream': ['MCC', 'Chocolate']}


# In[12]:


for cream in ice_cream_dict.values():
    print(cream)


# In[14]:


for key, value in ice_cream_dict.items():
    print(key,'=>', value)


# # Nested For Loops

# In[15]:


flavors = ['Vanilla', 'Chocolate', 'Cookie Dough']
toppings = ['Hot Fudge', 'Oreos', 'Marshmellows']


# In[16]:


for one in flavors:
    for two in toppings:
        print(one, 'topped with', two)


# # While Loops

# In[18]:


number = 0

while number < 5:
    print(number)
    number = number + 1


# # Break statement

# In[20]:


number = 0

while number < 5:
    print(number)
    if number == 3:
        break
    number = number + 1


# In[21]:


#Else Statement


# In[3]:


number = 0

while number < 5:
    print(number)
    if number == 6:
        break
    number = number + 1
else:
    print('No longer < 5')


# In[4]:


number = 0

while number < 5:
    number = number + 1
    if number == 3:
        continue
    print(number)
else:
    print('No longer < 5')


# # FUNCTIONS
# 

# In[5]:


def first_func():
    print('I did it')


# In[6]:


first_func()


# In[7]:


def number_squared(number):
    print(number**2)


# In[8]:


number_squared(5)


# In[9]:


def number_squared_custom(number,power):
    print(number**power)


# In[10]:


number_squared_custom(5,3)


# In[11]:


# Arbitrary Arguments


# In[16]:


args_tuple = (5,6,1,2,8)


def number_args(*number):
    print(number[0]*number[1])


# In[17]:


number_args(*args_tuple)


# In[ ]:


def number_squared_custom(number,power):
    print(number**power)


# In[18]:


number_squared_custom(power = 5, number = 3)


# In[30]:


def number_kwarg(**number):
    print('My number is: ' + number['integer'] + ', ' +'My other number: '+  number['integer2'])


# In[31]:


number_kwarg(integer = '3296', integer2 = '6719')


# In[ ]:





# # Converting Data Types

# In[32]:


num_int = 7
type(num_int)


# In[33]:


num_str = '7'
type(num_str)


# In[34]:


num_str_conv = int(num_str)


# In[35]:


num_sum = num_int + num_str_conv


# In[36]:


print(num_sum)


# In[ ]:





# # converting list sets and tuples

# In[38]:


list_type = [1,2,3]

type(list_type)


# In[40]:


type(tuple(list_type))


# In[41]:


#list to sets


# In[42]:


list_type = [1,2,3,3,2,1,2,3,2,1]


# In[44]:


type(set(list_type))


# In[45]:


#dictionaries


# In[46]:


dict_type = {'name': 'Josh', 'age': 28, 'hair': 'N/A'}


# In[47]:


dict_type.values()


# In[48]:


dict_type.keys()


# In[51]:


type(list(dict_type.keys()))


# In[52]:


#strings to list


# In[54]:


long_str = "I like to party"
list(long_str)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




