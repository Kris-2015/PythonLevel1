###############
## Problem 1 ##
###############

# Given the string
s = 'django'

# Using indexing to print out the following:

# d
    print (s[0])

# o
    print (s[5])

# djan
    print (s[0:4])

# 'jan'
    print (s[1:4])

# 'go'
    print (s[4:])

# Reverse the String
    # Step size method
    print (s[::-1])


###############
## Problem 2 ##
###############

# Given the nested list
l = [3, 7, [1, 4, 'hello']]
l[2][2] = 'good bye'


###############
## Problem 3 ##
###############

# Using key and indexing, grab the 'hello' from the following dictionaries:

d1 = {'simple_key': 'hello'}

print ('d1 result: ' + d1['simple_key'])

d2 = {'k1': {'k2': 'hello'}}

print ('d2 result: ' + d2['k1']['k2'])

d3 = {'k1': [{'nest_key': ['this is deep', ['hello']]}]}

print ('d3 result: ' + d3['k1'][0]['nest_key'][1][0])

    """
    Note:
        1. In List, concept is index number and value
        2. In Dictionaries, concept is key value
     """


###############
## Problem 4 ##
###############

# Use a set to find the unique values of the list below:
mylist = [1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]

[mylist[2] for number in mylist]

###############
## Problem 5 ##
###############

###############
## Problem 6 ##
###############
