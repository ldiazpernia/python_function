
# L1 = [1, 5, 2, 16, 32, 3, 54, 8, 100]
# L2 = [1, 3, 10, 2, 42, 2, 3, 4, 3]

# L3 = [x1 + x2 for (x1, x2) in list(zip(L1, L2)) if x1 > 10 and x2 < 5]
# print(L3)


things = [3, 5, -4, 7]
#accum = [x for x in things  ]
test  = list(map(lambda x : x+1 , things))
print (test)



def lengths(strings):
    """lengths takes a list of strings as input and returns a list of numbers that are the lengths
    of strings in the input list. Use manual accumulation!"""
    # fill in this function's definition to make the test pass.


