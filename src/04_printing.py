"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string 
method, and by using f-strings.
"""

x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"

# Use the 'format' string method to print the same thing

# Finally, print the same thing using an f-string
print('%s %s %s old style' % (x, y, z))
print('{} {} {} format syntax'.format(x, y, z))
print(f"{x} {y} {z} f syntax") #this doesn't work when running outside of virtualenv if you have python 2.7 on mac. 
