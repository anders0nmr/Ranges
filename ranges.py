#prints range object showing 0 to 100
#print(range(100))

#using range to create a list
#default start value is 0
#my_list =list(range(10))
#print(my_list)

#specifying starting point range
#starting point, ending point, steps
#odd = list(range(1,10,2))
#even = list(range(0,10,2))
#print(even)
#print(odd)

# my_string = 'abcdefghijklmnopqrstuvwxyz'
# print(my_string.index('e'))
# print(my_string[4])
#
# small_decimals = range(0, 10)
# print(small_decimals)
# print(small_decimals.index(3))
decimals = range (0, 100)
# print (decimals)
my_range = decimals[3:40:3]
print(my_range)
#
# for i in my_range:
#     print(i)
#
# for i in range(3, 40, 3):
#     print(i)

# decimals = range(0, 100)
# my_range = decimals[3:40:3]
# print(my_range == range(3, 40, 3))
# print (range(0,5,2) == range(0,6,2))

#Experiment with different ranges and slices to get a feel for how they work
#Remeber that you can print the range as well as iterating through it to print its values to check that your ranges are what you expected

my_range2 = range(0,10)
for i in my_range2:
    print(i)